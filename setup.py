from setuptools import setup, find_packages
import os

# Import configuration from pyproject.toml
try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # For older Python versions

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

project_config = config["project"]

# Read long description
long_description = ""
readme_file = project_config.get("readme", "README.md")
if os.path.exists(readme_file):
    with open(readme_file, "r") as f:
        long_description = f.read()

# Prepare entry points
scripts = project_config.get("scripts", {})
console_scripts = [f"{key}={value}" for key, value in scripts.items()]

# Setup configuration
setup(
    name=project_config["name"],
    version=project_config["version"],
    description=project_config.get("description", ""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=project_config["authors"][0]["name"],
    author_email=project_config["authors"][0]["email"],
    license=project_config["license"]["text"],
    classifiers=project_config.get("classifiers", []),
    python_requires=project_config["requires-python"],
    install_requires=config.get("dependencies", []),
    extras_require=config.get("optional-dependencies", {}),
    packages=find_packages(),  # Dynamically find all packages
    entry_points={"console_scripts": console_scripts},
)
