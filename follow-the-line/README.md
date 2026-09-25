# Follow the Line 🤿

**Underwater Robotics Computing Division: Introductory Project**

Our ROV has a camera pointing down at the pool floor, and there's an orange-red line of tape to follow.
Your mission: write the code that looks at a camera image and decides whether the robot should go
**LEFT**, **RIGHT**, **STRAIGHT**, or report that it's **LOST**.

Along the way you'll set up the same tools the team uses on the real robot code:

| Step | Guide | What you'll learn |
|---|---|---|
| 1 | [GitHub](docs/1-github.md) | Clone, branch, commit, push, pull requests |
| 2 | [Docker](docs/2-docker.md) | Everyone codes in the exact same environment, whatever laptop they have |
| 3 | [Jupyter](docs/3-jupyter.md) | Experiment with code one step at a time and see the results |
| 4 | [Follow the Line](docs/4-follow-the-line.md) | Computer vision with OpenCV, then turning vision into a steering decision |

Start with step 1 and go in order.

## What's in this folder

```
├── .devcontainer/        VS Code setup for Docker (step 2)
├── Dockerfile            Recipe for our environment: Python 3.11 + OpenCV + Jupyter
├── requirements.txt      Exact library versions everyone uses
├── images/               Fake underwater camera images, plus answers.json with the right answers
├── notebooks/            explore.ipynb: the guided walkthrough (step 3 and 4)
├── solutions/            _template.py: copy it and make it your own (step 4)
├── tests/                Checks every solution against every image
└── tools/                The script that made the images
```

## Why this project?

Following a line is a real task for underwater robots. The same steps you'll use here (color
thresholding, cleaning up a mask, finding blobs, filtering by shape) are the building blocks of
**path-following**, **docking**, and most other vision tasks the team works on.
