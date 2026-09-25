"""Follow the Line: <your name>

Copy this file to solutions/<your-github-username>.py and fill in the three
functions marked TODO. Work out each step in notebooks/explore.ipynb first,
then move your code here.

Check your work with:   pytest -k <your-github-username>
"""
import cv2
import numpy as np

# How far the line's center can be from the image center (as a fraction of
# half the image width) and still count as "straight". 0.15 = within 15%.
DEADBAND = 0.15


def find_line_mask(image_bgr: np.ndarray) -> np.ndarray:
    """Returns a mask the same height and width as the image:
    255 where a pixel looks like the orange-red line, 0 everywhere else.
    """
    # TODO: convert the image to HSV (cv2.cvtColor)
    # TODO: keep only line-colored pixels (cv2.inRange)
    # TODO: clean up the mask (cv2.morphologyEx)
    raise NotImplementedError("find_line_mask")


def find_line(mask: np.ndarray) -> np.ndarray | None:
    """Returns the contour of the line, or None if there is no line."""
    # TODO: find the outlines of every blob in the mask (cv2.findContours)
    # TODO: throw away blobs that are too small or not line-shaped
    #       (cv2.contourArea, cv2.minAreaRect)
    # TODO: return the biggest blob that's left, or None if nothing is left
    raise NotImplementedError("find_line")


def line_offset(contour: np.ndarray, image_width: int) -> float:
    """How far the line's center is from the image's center:
    -1.0 = far left edge, 0.0 = dead center, 1.0 = far right edge.
    """
    # TODO: find the x coordinate of the contour's center (cv2.moments)
    # TODO: turn it into a number from -1.0 to 1.0
    raise NotImplementedError("line_offset")


# You don't need to change anything below this line.
def steer(image_bgr: np.ndarray) -> str:
    """Decides which way the robot should go: "LEFT", "RIGHT", "STRAIGHT", or "LOST"."""
    mask = find_line_mask(image_bgr)
    contour = find_line(mask)
    if contour is None:
        return "LOST"
    offset = line_offset(contour, image_bgr.shape[1])
    if offset < -DEADBAND:
        return "LEFT"
    if offset > DEADBAND:
        return "RIGHT"
    return "STRAIGHT"
