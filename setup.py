from setuptools import find_packages, setup
from src.utils import get_requirements


setup(
    name="avatars-chatbots",
    version="0.0.2",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)