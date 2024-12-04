import re
import subprocess
import requests
from tabulate import tabulate

# Path to the requirements.txt file
requirements_path = "requirements.txt"

# Path to the README.md file
readme_path = "README.md"

# Define the regular expression pattern to match dependencies and versions
pattern = re.compile(r"^\s*([\w.-]+)\s*(==|>=|<=|!=|~=)?\s*([\w.+-]+)?\s*$")


# Function to extract dependencies from the requirements.txt file
def extract_dependencies(requirements_path):
    dependencies = set()
    with open(requirements_path, "r") as file:
        for line in file:
            match = pattern.match(line)
            if match:
                dependencies.add((match.group(1), match.group(3) or "N/A"))
    return dependencies


# Function to check if a package exists using pip
def package_exists(package_name):
    try:
        subprocess.run(["pip", "show", package_name], check=True,
                       stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


# Function to fetch the latest version and documentation URL from PyPI
def fetch_package_info(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["info"]["version"], data["info"]["home_page"]
    else:
        return None, None


# Function to update the README.md file with dependencies
def update_readme(dependencies):
    # Read the README content
    with open(readme_path, "r") as file:
        content = file.readlines()

    # Locate and replace the ## Dependencies section
    in_dependencies_section = False
    updated_content = []
    table_data = []
    section_found = False

    for line in content:
        if line.startswith("## Dependencies"):
            section_found = True
            in_dependencies_section = True
            # Add the header for the dependencies section
            updated_content.append("## Dependencies\n")
            dependencies = sorted(dependencies, key=lambda x: x[
                0])  # Sort dependencies alphabetically
            for dep, version in dependencies:
                latest_version, doc_url = fetch_package_info(dep)
                if latest_version:
                    table_data.append([dep, version, latest_version, doc_url])
                else:
                    table_data.append([dep, version, "N/A", "N/A"])
            # Add the table with dependencies
            updated_content.append(
                tabulate(table_data,
                         headers=["Package Name", "Required Version",
                                  "Latest Version", "Documentation URL"],
                         tablefmt="grid") + "\n")
        elif in_dependencies_section and line.strip() == "":
            # End of the dependencies section
            in_dependencies_section = False
        elif not in_dependencies_section:
            # Add all other lines outside the dependencies section
            updated_content.append(line)

    # If the section was not found, add it to the end
    if not section_found:
        updated_content.append("\n## Dependencies\n")
        dependencies = sorted(dependencies, key=lambda x: x[
            0])  # Sort dependencies alphabetically
        for dep, version in dependencies:
            latest_version, doc_url = fetch_package_info(dep)
            if latest_version:
                table_data.append([dep, version, latest_version, doc_url])
            else:
                table_data.append([dep, version, "N/A", "N/A"])
        updated_content.append(
            tabulate(table_data, headers=["Package Name", "Required Version",
                                          "Latest Version",
                                          "Documentation URL"],
                     tablefmt="grid") + "\n")

    # Write the updated content back to the README file
    with open(readme_path, "w") as file:
        file.writelines(updated_content)


# Main function to run the script
def main():
    dependencies = extract_dependencies(requirements_path)
    update_readme(dependencies)


# Entry point of the script
if __name__ == "__main__":
    main()
