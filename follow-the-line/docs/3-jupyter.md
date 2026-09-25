# 3. Jupyter: Experiment Step by Step

Computer vision is trial and error: change a number, look at the picture, change it again.
Re-running a whole script every time is slow. A **Jupyter notebook** splits code into **cells** you run
one at a time. Variables stay in memory between cells, and images show up right under the code.

Jupyter is already installed in our Docker image. There are two ways to use it.

## Option A: inside VS Code (recommended)

If you followed the Dev Container steps in [step 2](2-docker.md):

1. Open `notebooks/explore.ipynb`.
2. Click **Select Kernel** in the top right and choose **Python 3.11** (`/usr/local/bin/python`).
   The *kernel* is the Python program that runs your cells.
3. Click into the first code cell and press **Shift + Enter** to run it.

## Option B: in your browser

From the `follow-the-line` folder, start a container running Jupyter:

- **Windows (PowerShell):**

  ```powershell
  docker run -it --rm -p 8888:8888 -v "${PWD}:/workspace" follow-the-line
  ```

- **Mac / Linux:**

  ```bash
  docker run -it --rm -p 8888:8888 -v "$(pwd):/workspace" follow-the-line
  ```

The new parts:

- `-p 8888:8888` **forwards a port.** Jupyter listens on port 8888 inside the container, and this connects
  it to port 8888 on your computer so your browser can reach it.
- `-v <your folder>:/workspace` **mounts** your folder into the container, so your edits are saved to
  your real files. Without it, everything you change disappears when the container stops.

The terminal prints a link like `http://127.0.0.1:8888/tree?token=...`. Open it in your browser,
then open `notebooks/explore.ipynb`. Stop Jupyter with `Ctrl + C` in the terminal.

## Notebook basics

| Action | How |
|---|---|
| Run a cell | **Shift + Enter** |
| Add a cell below | Press `Esc`, then `B` |
| Restart (clear all variables) | **Restart** button (VS Code) or **Kernel → Restart** (browser) |

Cells run in the order **you** run them, not top to bottom. If things get weird, restart and run all cells again.

**Next:** [4. Follow the Line](4-follow-the-line.md)
