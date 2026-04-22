from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
PROTO_DIR = SCRIPT_DIR.parent
INPUTS_DIR = PROTO_DIR / "assets" / "entradas"
OUTPUT_PATH = INPUTS_DIR / "imagen_sintetica.png"


def build_synthetic_image(width: int = 900, height: int = 600) -> np.ndarray:
    """Construye una escena controlada para observar efectos morfologicos.

    La composicion combina:
    - un rectangulo con hueco interno, util para analizar cierre,
    - un circulo principal, util para observar cambio de contorno,
    - una brecha lineal horizontal, util para ver el efecto del kernel 5x1,
    - y pequenos puntos aislados, utiles para visualizar apertura y erosion.
    """
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # Figura principal rectangular con un hueco interior.
    cv2.rectangle(image, (80, 140), (320, 420), (0, 220, 220), thickness=-1)
    cv2.rectangle(image, (150, 210), (250, 320), (0, 0, 0), thickness=-1)

    # Circulo grande separado para contrastar comportamiento sobre bordes curvos.
    cv2.circle(image, (560, 250), 95, (255, 220, 0), thickness=-1)

    # Dos bloques con una brecha horizontal pequena: el kernel 5x1 deberia tender a unirla.
    cv2.rectangle(image, (460, 390), (540, 450), (255, 120, 0), thickness=-1)
    cv2.rectangle(image, (565, 390), (645, 450), (255, 120, 0), thickness=-1)

    # Ruido controlado para que apertura y erosion tengan un efecto visible.
    for center in ((700, 120), (735, 145), (770, 170), (190, 500), (230, 525)):
        cv2.circle(image, center, 8, (255, 255, 255), thickness=-1)

    return image


def save_synthetic_image(output_path: Path = OUTPUT_PATH) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image = build_synthetic_image()
    ok = cv2.imwrite(str(output_path), image)
    if not ok:
        raise RuntimeError(f"No se pudo guardar la imagen sintetica: {output_path}")
    return output_path


def main() -> None:
    output_path = save_synthetic_image()
    print(f"[ok] Imagen sintetica generada: {output_path}")


if __name__ == "__main__":
    main()
