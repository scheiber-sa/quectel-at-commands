from setuptools import setup

# Import configuration from pyproject.toml if possible
try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # For older Python versions

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

project_config = config["project"]

# Extract relevant fields from pyproject.toml
setup(
    name=project_config["name"],
    version=project_config["version"],
    description=project_config.get("description", ""),
    long_description=open(project_config.get("readme", "README.md")).read(),
    long_description_content_type="text/markdown",
    author=project_config["authors"][0]["name"],
    author_email=project_config["authors"][0]["email"],
    license=project_config["license"]["text"],
    classifiers=project_config.get("classifiers", []),
    python_requires=project_config["requires-python"],
    install_requires=config.get("dependencies", []),
    extras_require=config.get("project.optional-dependencies", {}),
    packages=["quectelatcommands"],  # Adjust as needed
    entry_points={"console_scripts": config.get("project.scripts", {})},
)
