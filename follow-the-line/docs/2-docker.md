# 2. Docker: Set Up the Environment

"It works on my computer" is the most common problem on any coding team. One person has Python 3.10,
another has 3.12, someone's OpenCV is a different version, and the same code behaves differently.

**Docker** fixes this. It runs our code inside a **container**: a small, isolated Linux system with
exactly the software we chose. Everyone's container is identical, whether they're on Windows, Mac, or Linux.

## Virtual machines vs. containers

| | Virtual machine | Container (Docker) |
|---|---|---|
| What it runs | A whole operating system, desktop included | Just the programs you need |
| Resources | Reserves a fixed chunk of memory and CPU | Uses resources only as needed, like a normal program |
| Start-up time | Minutes | Seconds |

## Images and containers

- A **Dockerfile** is a recipe.
- An **image** is what you get when you follow the recipe (`docker build`). Think of it as a frozen snapshot.
- A **container** is a running copy of an image (`docker run`). You can start and throw away as many as you like.

Here's our [Dockerfile](../Dockerfile), simplified:

```docker
FROM python:3.11-slim                   # start from an image that already has Python 3.11
RUN apt-get update && apt-get install -y git libglib2.0-0   # add system tools
COPY requirements.txt .
RUN pip install -r requirements.txt     # install our exact library versions
CMD ["jupyter", "notebook", ...]        # what runs when the container starts
```

`requirements.txt` lists exact versions (`opencv-python-headless==4.10.0.84`), so everyone gets the same libraries.

## Install Docker

Install **Docker Desktop**: https://www.docker.com/products/docker-desktop/

- **Windows:** the installer will ask to set up **WSL 2**. Say yes and restart when it asks.
- Open Docker Desktop and leave it running. The whale icon in your taskbar means Docker is ready.

## Let's do this

Run these from inside the `follow-the-line` folder. On Windows, use **PowerShell** for Docker commands.

1. **Build the image** (takes a minute or two the first time):

   ```bash
   docker build -t follow-the-line .
   ```

   `-t` gives the image a name (a *tag*). The `.` means "the Dockerfile is in this folder."

2. **Check that it's there:**

   ```bash
   docker image ls
   ```

3. **Start a container and look around:**

   ```bash
   docker run -it --rm follow-the-line bash
   ```

   - `-it` lets you type into the container's terminal.
   - `--rm` deletes the container when you leave (the image stays).
   - `bash` means "open a shell" instead of starting Jupyter.

4. **Prove you're inside:** run `python --version` (should say 3.11) and
   `python -c "import cv2; print(cv2.__version__)"` (should say 4.10.0).

5. **Leave** with `exit`.

## Docker + VS Code (what you'll use every day)

Typing `docker run` every time gets old. The **Dev Containers** extension opens the whole folder
*inside* the container, so VS Code's terminal, Python, and notebooks all run in our environment automatically.
The settings are already in [.devcontainer/devcontainer.json](../.devcontainer/devcontainer.json).

1. Open the `URT-Repo/follow-the-line` folder in VS Code (**File → Open Folder**). Open this folder, not the whole `URT-Repo`, so VS Code finds the Dev Container settings.
2. Install the **Dev Containers** extension (by Microsoft) from the Extensions tab on the left.
3. Press `Ctrl + Shift + P` (Mac: `Cmd + Shift + P`) and choose **Dev Containers: Reopen in Container**.
4. Wait for it to build. The bottom-left corner of VS Code will say **Dev Container: Follow the Line**.
5. Open a terminal in VS Code (`Ctrl + ~`) and run `python --version`. It should say **3.11**,
   even if your laptop has a different Python or none at all.

Your files still live on your computer; the container just borrows the folder. Git works like normal.

**Next:** [3. Jupyter](3-jupyter.md)
