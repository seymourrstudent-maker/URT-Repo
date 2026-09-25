"""Generates the fake underwater camera images in images/ and their answers.

You don't need to run this; the images are already in the repo. It's here so
you can see how they were made, or make new test cases.

    python tools/make_images.py
"""
import json
from pathlib import Path

import cv2
import numpy as np

W, H = 640, 480
IMAGES_DIR = Path(__file__).resolve().parent.parent / "images"

LINE_BGR = (40, 90, 230)  # orange-red tape on the pool floor
FISH_BGR = (35, 80, 225)  # a fish that is almost the same color as the tape
BUOY_BGR = (40, 200, 235)  # yellow
WEED_BGR = (60, 150, 40)  # green


def water(rng, brightness=1.0):
    """Blue-green pool floor with ripples of light, rocks, and camera noise."""
    y = np.linspace(0, 1, H)[:, None, None]
    top = np.array([150, 125, 35], dtype=float)
    bottom = np.array([105, 85, 20], dtype=float)
    img = np.broadcast_to(top * (1 - y) + bottom * y, (H, W, 3)).copy()

    # Caustics: the wavy light patterns you see on the bottom of a pool.
    yy, xx = np.mgrid[0:H, 0:W].astype(float)
    phase = rng.uniform(0, 2 * np.pi, 3)
    ripples = (
        np.sin(xx / 23 + np.sin(yy / 31 + phase[0]) * 2)
        + np.sin(yy / 19 + np.sin(xx / 27 + phase[1]) * 2)
        + np.sin((xx + yy) / 37 + phase[2])
    )
    img += (np.clip(ripples, 0, None) * 12)[..., None]

    # A few dark rocks.
    for _ in range(rng.integers(2, 6)):
        center = (int(rng.integers(0, W)), int(rng.integers(0, H)))
        axes = (int(rng.integers(10, 35)), int(rng.integers(8, 25)))
        shade = float(rng.uniform(0.55, 0.8))
        rock = img.copy()
        cv2.ellipse(rock, center, axes, float(rng.uniform(0, 180)), 0, 360, (0, 0, 0), -1)
        mask = rock[..., 0] == 0
        img[mask] *= shade

    return img * brightness


def blend(img, draw, color, strength=0.8):
    """Draws a shape onto the image, partly see-through like it's under water."""
    layer = np.zeros((H, W), np.uint8)
    draw(layer)
    mask = cv2.GaussianBlur(layer, (5, 5), 0).astype(float)[..., None] / 255 * strength
    return img * (1 - mask) + np.array(color, float) * mask


def line(x_bottom, x_top, y_start=H + 20, y_end=-20, thickness=36):
    return lambda layer: cv2.line(layer, (x_bottom, y_start), (x_top, y_end), 255, thickness)


def fish(x, y, facing=1):
    def draw(layer):
        cv2.ellipse(layer, (x, y), (38, 18), 0, 0, 360, 255, -1)
        tail = np.array([[x - facing * 34, y], [x - facing * 60, y - 20], [x - facing * 60, y + 20]])
        cv2.fillPoly(layer, [tail], 255)

    return draw


def circle(x, y, r):
    return lambda layer: cv2.circle(layer, (x, y), r, 255, -1)


def seaweed(x, y):
    def draw(layer):
        for dx in (-14, 0, 14):
            pts = np.array([[x + dx + int(8 * np.sin(t / 12)), y - t] for t in range(0, 110, 5)])
            cv2.polylines(layer, [pts], False, 255, 7)

    return draw


def finish(img, rng, brightness=1.0):
    """Water absorbs red light, the camera adds noise, and the edges are a bit dark."""
    img = img * np.array([1.0, 0.96, 0.85])
    yy, xx = np.mgrid[0:H, 0:W]
    vignette = 1 - 0.35 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) / 2
    img = img * vignette[..., None] * brightness
    img += rng.normal(0, 6, img.shape)
    img = cv2.GaussianBlur(np.clip(img, 0, 255).astype(np.uint8), (3, 3), 0)
    return img


# name: (list of (shape, color), brightness, answer, explanation)
CASES = {
    "01_center": ([(line(320, 320), LINE_BGR)], 1.0, "STRAIGHT", "The line is right in the middle."),
    "02_left": ([(line(150, 170), LINE_BGR)], 1.0, "LEFT", "The line is on the left side."),
    "03_right": ([(line(500, 480), LINE_BGR)], 1.0, "RIGHT", "The line is on the right side."),
    "04_slightly_right": (
        [(line(345, 355), LINE_BGR)],
        1.0,
        "STRAIGHT",
        "The line is only a little right of center, inside the deadband.",
    ),
    "05_diagonal_center": (
        [(line(230, 410), LINE_BGR)],
        1.0,
        "STRAIGHT",
        "The line is tilted, but its center is in the middle.",
    ),
    "06_diagonal_left": (
        [(line(60, 260), LINE_BGR)],
        1.0,
        "LEFT",
        "The line is tilted, and its center is on the left.",
    ),
    "07_murky_left": (
        [(line(190, 190), LINE_BGR)],
        0.5,
        "LEFT",
        "Dark, murky water. Is your brightness (V) threshold too high?",
    ),
    "08_fish_and_line": (
        [(line(480, 500), LINE_BGR), (fish(140, 300), FISH_BGR)],
        1.0,
        "RIGHT",
        "The line is on the right; the orange fish on the left is not the line.",
    ),
    "09_seaweed_and_buoy": (
        [(line(320, 320), LINE_BGR), (seaweed(160, 420), WEED_BGR), (circle(470, 150, 40), BUOY_BGR)],
        1.0,
        "STRAIGHT",
        "The line is in the middle; ignore the green seaweed and yellow buoy.",
    ),
    "10_fish_only": (
        [(fish(420, 260, facing=-1), FISH_BGR)],
        1.0,
        "LOST",
        "There is no line, only a fish. A fish is not line-shaped.",
    ),
    "11_short_line_and_big_buoy": (
        [(line(200, 200, y_start=240), LINE_BGR), (circle(480, 330, 65), BUOY_BGR)],
        1.0,
        "LEFT",
        "The line (top-left) is smaller than the yellow buoy. Is your hue range too wide?",
    ),
    "12_empty": ([], 1.0, "LOST", "There's nothing here but water and rocks."),
    "13_far_right": ([(line(595, 610), LINE_BGR)], 1.0, "RIGHT", "The line is at the far right edge."),
}


def main():
    IMAGES_DIR.mkdir(exist_ok=True)
    answers = {}
    for index, (name, (shapes, brightness, answer, why)) in enumerate(CASES.items()):
        rng = np.random.default_rng(index)
        img = water(rng)
        for draw, color in shapes:
            img = blend(img, draw, color)
        img = finish(img, rng, brightness)
        cv2.imwrite(str(IMAGES_DIR / f"{name}.png"), img)
        answers[f"{name}.png"] = {"answer": answer, "why": why}
    (IMAGES_DIR / "answers.json").write_text(json.dumps(answers, indent=2) + "\n")
    print(f"Wrote {len(answers)} images to {IMAGES_DIR}")


if __name__ == "__main__":
    main()
