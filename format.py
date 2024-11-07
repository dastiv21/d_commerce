import json
import os
import subprocess

# Function to read configuration from config.json
def read_config():
    try:
        with open('config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        return {}

# Function to get project metadata using git
def get_project_metadata():
    metadata = {}
    try:
        metadata['authors'] = subprocess.check_output(['git', 'log', '--format="%aN <%aE>"', '-n', '1']).decode().strip()
        metadata['dependencies'] = subprocess.check_output(['pip', 'freeze']).decode().strip()
    except subprocess.CalledProcessError:
        pass
    return metadata

# Function to fill in the README template
def generate_readme(config, metadata):
    readme_template = """
# {project_title}

## Project Description
{project_description}

## Installation
{installation}

## Usage
{usage}

## Authors
{authors}

## Dependencies
{dependencies}

## License
{license}
    """

    readme_content = readme_template.format(
        project_title=config.get('project_title', 'Project Title'),
        project_description=config.get('project_description', 'Brief description of the project.'),
        installation=config.get('installation', 'Steps to install.'),
        usage=config.get('usage', 'How to use the project.'),
        authors=config.get('authors', metadata.get('authors', 'Author Names')),
        dependencies=config.get('dependencies', metadata.get('dependencies', 'List of dependencies.')),
        license=config.get('license', 'Project License')
    )

    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)

# Main function to run the script
if __name__ == '__main__':
    config = read_config()
    metadata = get_project_metadata()
    generate_readme(config, metadata)