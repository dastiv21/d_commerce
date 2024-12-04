import subprocess
from git import Repo
import os

# Path to the Git repository
repo_path = "./"


# Update the README.md file with recent commits and test results
def update_readme():
    # Initialize the Git repository
    repo = Repo(repo_path)
    git = repo.git

    # Get the latest commit hash
    latest_commit = git.log("-1", "--pretty=format:%H")

    # Get the test results (replace 'pytest' with your test command)
    test_results = subprocess.run(
        ["pytest", "--junitxml=test-results.xml"], capture_output=True,
        text=True
    )
    test_status = "Passed" if test_results.returncode == 0 else "Failed"

    # Update the README.md file
    readme_path = os.path.join(repo_path, "README.md")
    with open(readme_path, "a") as readme:
        readme.write(f"\n## Recent Commit\n{latest_commit}\n")
        readme.write(f"## Test Results\n{test_status}\n")


# Run the function to update the README.md file
update_readme()