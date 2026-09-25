# Start from an official image that already has Python 3.11 installed.
FROM python:3.11-slim

# System packages: git (so VS Code's source control works inside the container)
# and libglib (a small library OpenCV needs).
RUN apt-get update \
    && apt-get install -y --no-install-recommends git libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Install the exact library versions listed in requirements.txt.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Jupyter runs on port 8888. By default, starting the container starts Jupyter.
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
