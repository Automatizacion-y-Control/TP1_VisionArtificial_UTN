from __future__ import annotations

import argparse
import importlib.util
from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUTS_DIR = PROJECT_ROOT / "c_prototipado" / "assets" / "entradas"
OUTPUTS_DIR = PROJECT_ROOT / "c_prototipado" / "assets" / "salidas"
SCRIPTS_DIR = PROJECT_ROOT / "c_prototipado" / "scripts"


@dataclass(frozen=True)
class CaseConfig:
    name: str
    input_path: Path
    output_dir: Path


REAL_CASE = CaseConfig(
    name="real",
    input_path=INPUTS_DIR / "imagen_real.png",
    output_dir=OUTPUTS_DIR / "real",
)

SYNTHETIC_CASE = CaseConfig(
    name="sintetica",
    input_path=INPUTS_DIR / "imagen_sintetica.png",
    output_dir=OUTPUTS_DIR / "sintetica",
)


KERNEL_3X3 = np.ones((3, 3), dtype=np.uint8)
KERNEL_5X1 = np.ones((1, 5), dtype=np.uint8)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Pipeline del TP1 de Vision Artificial.")
    parser.add_argument(
        "--case",
        choices=("real", "sintetica", "all"),
        default="real",
        help="Caso a procesar.",
    )
    return parser.parse_args()


def load_synthetic_generator():
    """Carga el generador sintetico sin exigir que scripts/ sea un paquete Python."""
    generator_path = SCRIPTS_DIR / "generar_imagen_sintetica.py"
    spec = importlib.util.spec_from_file_location("generar_imagen_sintetica", generator_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No se pudo cargar el generador sintetico: {generator_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def ensure_output_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def load_image(image_path: Path) -> np.ndarray:
    image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"No se pudo leer la imagen: {image_path}")
    return image


def save_image(path: Path, image: np.ndarray) -> None:
    ok = cv2.imwrite(str(path), image)
    if not ok:
        raise RuntimeError(f"No se pudo guardar la imagen: {path}")


def save_original(image: np.ndarray, output_dir: Path) -> None:
    save_image(output_dir / "01_original.png", image)


def to_grayscale(image: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_otsu(gray: np.ndarray) -> tuple[float, np.ndarray]:
    threshold, binary = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    return threshold, binary


def create_histogram_image(gray: np.ndarray, otsu_threshold: float) -> np.ndarray:
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256]).flatten()
    hist = hist / max(hist.max(), 1.0)

    width = 512
    height = 400
    margin = 30
    canvas = np.full((height, width, 3), 255, dtype=np.uint8)

    plot_width = width - (2 * margin)
    plot_height = height - (2 * margin)
    bin_width = plot_width / 256.0

    for idx in range(255):
        x1 = int(margin + idx * bin_width)
        x2 = int(margin + (idx + 1) * bin_width)
        y1 = int(height - margin - hist[idx] * plot_height)
        y2 = int(height - margin - hist[idx + 1] * plot_height)
        cv2.line(canvas, (x1, y1), (x2, y2), (50, 50, 50), 1)

    threshold_x = int(margin + otsu_threshold * bin_width)
    cv2.line(canvas, (threshold_x, margin), (threshold_x, height - margin), (0, 0, 255), 2)
    cv2.rectangle(canvas, (margin, margin), (width - margin, height - margin), (0, 0, 0), 1)

    cv2.putText(
        canvas,
        f"Otsu = {otsu_threshold:.2f}",
        (margin + 8, margin + 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (0, 0, 255),
        1,
        cv2.LINE_AA,
    )

    return canvas


def apply_morphology(binary: np.ndarray, kernel: np.ndarray) -> dict[str, np.ndarray]:
    return {
        "erosion": cv2.erode(binary, kernel, iterations=1),
        "dilatacion": cv2.dilate(binary, kernel, iterations=1),
        "apertura": cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel),
        "cierre": cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel),
    }


def save_kernel_results(results: dict[str, np.ndarray], output_dir: Path, start_index: int, suffix: str) -> None:
    ordered_names = ("erosion", "dilatacion", "apertura", "cierre")
    for offset, name in enumerate(ordered_names):
        filename = f"{start_index + offset:02d}_{name}_{suffix}.png"
        save_image(output_dir / filename, results[name])


def prepare_case_input(case: CaseConfig) -> None:
    """Garantiza que cada caso tenga su entrada disponible antes del procesamiento."""
    if case.name != "sintetica":
        return

    generator = load_synthetic_generator()
    generator.save_synthetic_image(case.input_path)


def process_case(case: CaseConfig) -> None:
    ensure_output_dir(case.output_dir)
    prepare_case_input(case)
    image = load_image(case.input_path)
    gray = to_grayscale(image)
    otsu_threshold, binary = apply_otsu(gray)
    histogram = create_histogram_image(gray, otsu_threshold)

    morph_3x3 = apply_morphology(binary, KERNEL_3X3)
    morph_5x1 = apply_morphology(binary, KERNEL_5X1)

    save_original(image, case.output_dir)
    save_image(case.output_dir / "02_grises.png", gray)
    save_image(case.output_dir / "03_binaria_otsu.png", binary)
    save_image(case.output_dir / "04_histograma_otsu.png", histogram)
    save_kernel_results(morph_3x3, case.output_dir, start_index=5, suffix="3x3")
    save_kernel_results(morph_5x1, case.output_dir, start_index=9, suffix="5x1")

    print(f"[ok] Caso procesado: {case.name}")
    print(f"     Entrada: {case.input_path}")
    print(f"     Salidas: {case.output_dir}")


def resolve_cases(case_name: str) -> tuple[CaseConfig, ...]:
    if case_name == "real":
        return (REAL_CASE,)
    if case_name == "sintetica":
        return (SYNTHETIC_CASE,)
    return (REAL_CASE, SYNTHETIC_CASE)


def main() -> None:
    args = parse_args()
    for case in resolve_cases(args.case):
        process_case(case)


if __name__ == "__main__":
    main()
