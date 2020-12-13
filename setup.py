from pathlib import Path
from setuptools import setup

README_FILE = Path.cwd() / "README.md"

setup(
    name="enum4linux.py",
    version="0.0.0a",
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
    entry_points={
        "console_scripts": [
            "enum4linux=enum4linux.__main__:main"
        ]
    }
)
