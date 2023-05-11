def get_requirements(filename: str) -> list[str]:
    """
    Reads requirements file and returns list of packages.
    """
    with open(filename, "r") as file:
        requirements = file.read()
    return [package.strip() for package in requirements.split("\n") if package not in "-e ."]
