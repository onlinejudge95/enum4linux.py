from pathlib import Path

from setuptools import setup

from enum4linux import __version__ as VERSION


CURRENT_WORKING_DIR = Path.cwd()
README_FILE = CURRENT_WORKING_DIR / "README.md"
REQUIREMENTS_FILE = CURRENT_WORKING_DIR / "requirements.txt"


setup(
    name="enum4linux.py",
    version=VERSION,
    description="Port for enum4linux perl script",
    long_description_content_type="text/markdown",
    long_description=README_FILE.read_text(),
    url="https://github.com/onlinejudge95/enum4linux.py",
    author="onlinejudge95",
    author_email="onlinejudge95@gmail.com",
    license="GNU GPLv2",
    packages=[
        "enum4linux",
    ],
    install_requires=REQUIREMENTS_FILE.read_text(),
    entry_points={
        "console_scripts": ["enum4linux=enum4linux.__main__:entrypoint"]
    },
)
