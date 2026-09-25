"""Tests every file in solutions/ (except the template) against every image.

Run all tests:          pytest
Run only your tests:    pytest -k <your-github-username>
"""
import importlib.util
import json
from functools import cache
from pathlib import Path

import cv2
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = ROOT / "images"
ANSWERS = json.loads((IMAGES_DIR / "answers.json").read_text())
SOLUTIONS = sorted(
    path for path in (ROOT / "solutions").glob("*.py") if not path.name.startswith("_")
)
SOLUTION_IDS = [path.stem for path in SOLUTIONS]


@cache
def load_solution(path):
    spec = importlib.util.spec_from_file_location(f"solutions.{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@cache
def load_image(name):
    return cv2.imread(str(IMAGES_DIR / name))


@pytest.mark.parametrize("solution", SOLUTIONS, ids=SOLUTION_IDS)
def test_mask_is_black_and_white(solution):
    image = load_image("01_center.png")
    mask = load_solution(solution).find_line_mask(image)
    assert mask.shape == image.shape[:2], "The mask should be the same height and width as the image"
    assert set(np.unique(mask)) <= {0, 255}, "The mask should only contain 0 and 255"


@pytest.mark.parametrize("solution", SOLUTIONS, ids=SOLUTION_IDS)
@pytest.mark.parametrize("image_name", sorted(ANSWERS))
def test_steer(solution, image_name):
    expected = ANSWERS[image_name]
    got = load_solution(solution).steer(load_image(image_name))
    assert got == expected["answer"], f"{image_name}: expected {expected['answer']}, got {got}. Hint: {expected['why']}"
