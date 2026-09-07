"""Commit and push changes made to fundamental_ques.py."""

from pathlib import Path
import shutil
import subprocess
import sys


SCRIPT_DIR = Path(__file__).resolve().parent
GIT_EXECUTABLE = shutil.which("git") or r"C:\Program Files\Git\cmd\git.exe"


def run_git(*args: str) -> str:
	"""Run a Git command from the repository root."""
	result = subprocess.run(
		[GIT_EXECUTABLE, *args],
		cwd=SCRIPT_DIR,
		check=True,
		text=True,
		capture_output=True,
	)
	return result.stdout.strip()


REPO_ROOT = Path(run_git("rev-parse", "--show-toplevel"))
TARGET_FILE = SCRIPT_DIR.parent / "fundamental_ques.py"


def main() -> None:
	if not TARGET_FILE.is_file():
		print(f"File not found: {TARGET_FILE}", file=sys.stderr)
		raise SystemExit(1)

	relative_target = TARGET_FILE.relative_to(REPO_ROOT)
	status = run_git("status", "--porcelain", "--", str(relative_target))
	if not status:
		print("No changes to fundamental_ques.py.")
		return

	run_git("add", "--", str(relative_target))
	message = "Update fundamental_ques.py"
	run_git("commit", "-m", message)
	run_git("push")
	print("Changes committed and pushed successfully.")


if __name__ == "__main__":
	main()
