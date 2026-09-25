# Intro to GitHub: Member Cards

Welcome to the Underwater Robotics Computing Division! Your first task is to add
yourself to the team roster, **using the same workflow we use for real robot code**:

> clone → branch → change → commit → push → pull request → review → merge

When you're done, `python roster.py` will show you in the team roster.

---

## Before the session

1. **Accept your invite** to collaborate on the repo (check your email or github.com/notifications).
2. **Install Git:** https://git-scm.com/downloads (Windows: keep all the default options).
3. **Install Python 3:** https://www.python.org/downloads/ (Windows: check **"Add python.exe to PATH"**).
4. **Install VS Code:** https://code.visualstudio.com (Windows: check **"Add to PATH"** during setup).
5. **Tell Git who you are.** Open a terminal (Windows: *Git Bash*) and run:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "the-email-on-your-github-account@example.com"
   ```

---

## Step 1: Clone the repo

Cloning downloads a copy of the repo to your computer:

```bash
git clone https://github.com/seymourrstudent-maker/URT-Repo.git
cd URT-Repo/member-cards
```

## Step 2: Make a branch

A branch is your own copy of the code where you can make changes without affecting anyone else.
Never work directly on `main`.

```bash
git switch -c add-<your-github-username>
```

## Step 3: Make your member card

Copy the template and name the copy after your GitHub username:

```bash
cp members/_TEMPLATE.yml members/<your-github-username>.yml
```

Open the folder in VS Code:

```bash
code .
```

Open `members/<your-github-username>.yml` from the file list on the left and replace every `<...>` value.
Save the file (Ctrl+S, or Cmd+S on Mac).

> **Tip:** VS Code has a built-in terminal (**Terminal → New Terminal**), so you can run the rest of
> the commands there instead of switching windows. On Windows, pick **Git Bash** from the dropdown
> next to the **+** in the terminal panel.

Then check your card:

```bash
python roster.py
```

(On Mac/Linux, you may need `python3` instead of `python`.) Fix anything it complains about.

## Step 4: Commit

A commit is a saved snapshot of your changes, with a message describing what you did.

```bash
git status                          # see what changed
git add members/<your-github-username>.yml
git commit -m "Add <your name>'s member card"
```

## Step 5: Push

Pushing uploads your branch to GitHub.

```bash
git push -u origin add-<your-github-username>
```

The first time, a window may pop up asking you to sign in to GitHub. That's normal.

## Step 6: Open a pull request (PR)

1. Go to the repo on GitHub. You'll see a yellow banner. Click **Compare & pull request**.
2. Give it a title like `Add <your name>`, then click **Create pull request**.
3. Wait for the check at the bottom of the PR to finish:
   - ✅ **Green check:** your card is valid.
   - ❌ **Red X:** click **Details** to see what's wrong. Fix it on your computer, then
     `git add`, `git commit`, and `git push` again. The PR updates automatically.

## Step 7: Review and merge

A lead will review your PR and merge it into `main`. Then update your copy of the repo:

```bash
git switch main
git pull
python roster.py
```

You should see yourself, and everyone else who has been merged, in the roster. 🎉

---

## Stretch goals

- **Review a teammate's PR.** Open their PR, go to **Files changed**, and leave a comment on a line.
- **Make a second change.** Add a new line to your card (like `favorite_language: Python`),
  and take it through the whole branch → PR → merge loop again, this time without the guide.
- **Look at the robot.** Open `.github/workflows/member-cards.yml` (at the top of the repo) and `roster.py` to see how
  GitHub automatically checks every PR.

## Cheat sheet

| Command | What it does |
|---|---|
| `git clone <url>` | Download a repo |
| `git status` | Show what has changed |
| `git switch -c <name>` | Create a new branch and switch to it |
| `git switch <name>` | Switch to an existing branch |
| `git add <file>` | Stage a file to be committed |
| `git commit -m "msg"` | Save a snapshot of staged changes |
| `git push` | Upload your commits to GitHub |
| `git pull` | Download the latest commits from GitHub |
| `git log --oneline` | Show commit history |
