"""Packaging for taagraels"""

import os

from setuptools import find_packages, setup

###############################################################################
base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "src")
###############################################################################

name = "checkio"
# get version
version = {}
with open(os.path.join(src_dir, name, "version.py")) as f:
    exec(f.read(), version)

# get long_description
with open(os.path.join(base_dir, "README.md")) as f:
    long_description = f.read()

###############################################################################

requires = ["click"]
test_requires = ["pytest"]

setup(
    name=name,
    version=version["__version__"],
    keywords="checkio solution python code",
    description="zoido's checkio sollution",
    long_description=long_description,
    author="Luboš Pokorný",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=requires,
    extras_require={
        "test": test_requires,
    },
    setup_requires=["pytest-runner"], )
