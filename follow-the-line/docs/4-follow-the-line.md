# 4. Follow the Line

Now the real project. You'll build a small computer vision pipeline:

```
camera image → HSV → mask → clean up → find blobs → pick the line → find its center → LEFT / RIGHT / STRAIGHT / LOST
```

## Part 1: Explore in the notebook

Open `notebooks/explore.ipynb` and work through it top to bottom. It explains each step and has
three **🔧 TODO** spots for you to fill in:

1. The color range that keeps only the line.
2. The size and shape limits that tell the line apart from fish and buoys.
3. The math to find how far the line is from the center.

The last cell tests your code on every image. Aim for **13/13**.

The test images include some traps: murky water, an orange fish, a yellow buoy, and a short line next
to a big buoy. If one fails, the image name is a hint.

## Part 2: Move your code into the codebase

Notebooks are for experimenting; the robot runs regular Python files. Teams keep them separate
so the real code stays clean and testable.

1. **Make your solution file:**

   ```bash
   cp solutions/_template.py solutions/<your-github-username>.py
   ```

2. **Fill in its three functions** with the code from your notebook:

   | Notebook | Solution file |
   |---|---|
   | `make_mask` + `clean` | `find_line_mask` |
   | `pick_line` | `find_line` |
   | `offset_of` | `line_offset` |

3. **Run the tests** (in the VS Code terminal inside the Dev Container):

   ```bash
   pytest -k <your-github-username>
   ```

   Each failing test tells you which image went wrong and gives a hint. Keep going until everything passes.

## Part 3: Submit it with a pull request

```bash
git add solutions/<your-github-username>.py
git commit -m "Add <your name>'s line follower"
git push -u origin <your-github-username>-solution
```

Then open a pull request on GitHub. GitHub runs the same tests on your code:
✅ means you're ready for review, ❌ means click **Details** to see what failed.
Fix it, commit, and push again; the PR updates by itself.

## Stretch goals

- **Look ahead.** `cv2.fitLine` gives the line's angle. Can you start turning *before* the line
  drifts off-center?
- **True red tape.** Real red wraps around the hue scale: it's near 0 **and** near 179. Make two
  masks and combine them with `cv2.bitwise_or`.
- **Make a harder test.** Add a case to `tools/make_images.py` (a bent line, two lines, bubbles...),
  run `python tools/make_images.py`, and see if your solution survives.
- **Review a teammate's PR.** Read their code in **Files changed** and leave a helpful comment.

## Rule-based vision vs. AI

We solved this with hand-written rules (color ranges, shape limits). The other option is training an
AI model on lots of labeled images. The two approaches have different strengths:

| | Rules (what we did) | AI model |
|---|---|---|
| Training data needed | Almost none | Lots |
| Speed | Fast | Usually slower |
| When it's wrong, can you tell why? | Yes: check the mask, check the numbers | Often hard to tell |
| Handles surprises (new lighting, new objects) | Only the cases you thought of | Better, if trained well |

Real robots often use both.
