import os
import sys
import subprocess


def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command: {command}\n{result.stderr}")
        sys.exit(1)
    else:
        print(result.stdout)


def submit(branch):
    commands = [
        f"git checkout -b cs50/problems/2022/python/{branch}",
        f"git add {branch}.py",
        f'git commit -m "automated submission for branch cs50/problems/2022/python/{branch}"',
        f"git push --set-upstream https://github.com/me50/Nottletottle.git cs50/problems/2022/python/{branch}",
    ]

    for command in commands:
        run_command(command)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: submit <branch>")
        sys.exit(1)

    branch_name = sys.argv[1]
    submit(branch_name)
