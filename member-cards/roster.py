"""Reads every member card in members/ and prints the team roster.

Run it with:   python roster.py

If any card has a problem, the script lists what is wrong and exits with an
error. GitHub Actions runs this same script on every pull request, so a card
with a problem shows up as a red X on the PR.
"""
import os
import sys
import textwrap
from pathlib import Path

MEMBERS_DIR = Path(__file__).parent / "members"
REQUIRED = ["name", "github", "major", "year", "fun_fact", "preferred_project"]
YEARS = ["freshman", "sophomore", "junior", "senior", "grad"]
PROJECTS = [
    "sensors",
    "simulation",
    "computer-vision",
    "autonomy",
    "controls",
    "onboard-systems",
    "ai",
    "undecided",
]


def read_card(path):
    """Turns a file of 'key: value' lines into a dictionary."""
    card = {}
    problems = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            problems.append(f"line {number} should look like 'key: value' but is: {line}")
            continue
        key, value = line.split(":", 1)
        card[key.strip().lower()] = value.strip()
    return card, problems


def check_card(path, card):
    """Returns a list of everything wrong with one card (empty list = all good)."""
    problems = []
    for key in REQUIRED:
        if not card.get(key):
            problems.append(f"'{key}' is missing or empty")
    for key, value in card.items():
        if value.startswith("<"):
            problems.append(f"'{key}' still has the template placeholder: {value}")
    github = card.get("github", "")
    if github and not github.startswith("<") and github.lower() != path.stem.lower():
        problems.append(f"file should be named {github}.yml to match your GitHub username")
    year = card.get("year", "")
    if year and not year.startswith("<") and year.lower() not in YEARS:
        problems.append(f"'year' should be one of: {', '.join(YEARS)}")
    projects = card.get("preferred_project", "")
    if projects and not projects.startswith("<"):
        for project in projects.split(","):
            if project.strip().lower() not in PROJECTS:
                problems.append(
                    f"'{project.strip()}' isn't a project area. Pick from: {', '.join(PROJECTS)}"
                )
    return problems


def print_card(card):
    """Prints one member as a block, one answer per line, wrapping long answers."""
    print(f"\n{card['name']} (@{card['github']})")
    details = {key: value for key, value in card.items() if key not in ("name", "github")}
    if "year" in details:
        details["year"] = details["year"].capitalize()
    labels = {key: key.replace("_", " ").capitalize() + ":" for key in details}
    width = max(len(label) for label in labels.values()) + 1
    for key, value in details.items():
        print(textwrap.fill(
            value,
            width=76,
            initial_indent="  " + labels[key].ljust(width),
            subsequent_indent="  " + " " * width,
        ))


def main():
    cards = []
    all_problems = {}

    for path in sorted(MEMBERS_DIR.iterdir(), key=lambda p: p.name.lower()):
        if path.name.startswith("_"):
            continue  # skip the template
        if path.suffix != ".yml":
            all_problems[path.name] = ["member cards must end in .yml"]
            continue
        card, problems = read_card(path)
        problems += check_card(path, card)
        if problems:
            all_problems[path.name] = problems
        else:
            cards.append(card)

    table = ["| Name | GitHub | Major | Year | Preferred project | Fun fact |", "|---|---|---|---|---|---|"]
    for card in cards:
        table.append(
            f"| {card['name']} | @{card['github']} | {card['major']} "
            f"| {card['year'].capitalize()} | {card['preferred_project']} | {card['fun_fact']} |"
        )

    print(f"Underwater Robotics - Computing Division ({len(cards)} members)")
    for card in cards:
        print_card(card)

    # On GitHub Actions, also show the roster on the run's summary page.
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as summary:
            summary.write(f"## Computing Division roster ({len(cards)} members)\n\n")
            summary.write("\n".join(table) + "\n")

    if all_problems:
        print("\nSome member cards need fixing:")
        for filename, problems in all_problems.items():
            print(f"\n  members/{filename}")
            for problem in problems:
                print(f"    - {problem}")
        sys.exit(1)

    print("\nAll member cards look good!")


if __name__ == "__main__":
    main()
