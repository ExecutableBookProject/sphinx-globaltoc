import os

from setuptools import setup, find_packages
from sphinx_globaltoc import __version__

with open("./README.rst", "r") as ff:
    readme_text = ff.read()

setup(
    name="sphinx-globaltoc",
    version=__version__,
    description="Add a toggle button to items on a page.",
    long_description=readme_text,
    long_description_content_type="text/x-rst",
    author="Chris Holdgraf",
    author_email="choldgraf@berkeley.edu",
    url="https://github.com/ExecutableBookProject/sphinx-globaltoc",
    license="MIT License",
    packages=find_packages(),
    install_requires=["setuptools", "wheel", "sphinx"],
    extras_require={"sphinx": ["sphinx"]},
    classifiers=["License :: OSI Approved :: MIT License"],
)
