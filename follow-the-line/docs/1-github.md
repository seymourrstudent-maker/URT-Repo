# 1. GitHub: Set Up the Repository

GitHub is where all of our code lives. Git keeps track of every change, so many people can work on
the same code without overwriting each other.

## Before you start

- Accept your invite to collaborate on the repo (check your email or github.com/notifications).
- Install **Git**: https://git-scm.com/downloads (Windows: keep all the default options).
- Install **VS Code**: https://code.visualstudio.com
- Tell Git who you are (open a terminal; on Windows use **Git Bash**):

  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "the-email-on-your-github-account@example.com"
  ```

## Clone the repository

`git clone` downloads your own copy of the repo. Our repo, **URT-Repo**, holds several projects in
separate folders; this one is in `follow-the-line/`.

```bash
git clone https://github.com/seymourrstudent-maker/URT-Repo.git
cd URT-Repo/follow-the-line
```

Already cloned URT-Repo for the member cards? Don't clone again. Just get the latest version instead:

```bash
cd URT-Repo
git switch main
git pull
cd follow-the-line
```

## Make a branch

A **branch** is your own line of work. You can change anything on your branch without breaking `main`,
the version everyone else uses.

```bash
git switch -c <your-github-username>-solution
```

```
main ──●──●──●──────────────●──   (everyone's working code)
             \              /
              ●──●──●──●───        (your branch, merged back in with a pull request)
```

## The loop you'll use every day

```bash
git status                       # what did I change?
git add <file>                   # stage a file: "include this in my next save"
git commit -m "What I did"       # save a snapshot, with a message
git push                         # upload your commits to GitHub
```

The **first** time you push a new branch, GitHub doesn't know about it yet, so use `-u`:

```bash
git push -u origin <your-github-username>-solution
```

`-u` (short for `--set-upstream`) links your local branch to one on GitHub, so after that a plain
`git push` knows where to go. A window may pop up asking you to sign in to GitHub. That's normal.

## Pull requests

When your work is ready, go to the repo on GitHub and click **Compare & pull request**.
A **pull request (PR)** asks to merge your branch into `main`. GitHub runs the tests automatically,
a lead reviews your code, and then it gets merged.

You'll do this for real at the end of [step 4](4-follow-the-line.md).

## Dive deeper

[Learn Git Branching](https://learngitbranching.js.org/) is the best interactive way to understand
branches, merging, and rebasing.

**Next:** [2. Docker](2-docker.md)
