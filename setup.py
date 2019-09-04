"""setup.py"""
from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="cpu-load-generator",
    download_url="git+ssh://git@github.com/aliculPix4D/cpu-load-generator.git ",
    install_requires=requirements,
    setup_requires=["setuptools_scm"],
    packages=["cpu_load_generator"],
    entry_points={"console_scripts": ["cpu_load=cpu_load_generator.cpu_load:main"]},
)
