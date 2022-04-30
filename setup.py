"""A setuptools based setup module"""
import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="csv2db",
    version="0.3.0-beta",
    description="CLI for uploading a csv file to a database table",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fgomezotero/csv2db",
    author="Franklin Gómez Otero",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[
        "Click",
        "SQLAlchemy",
        "psycopg2-binary",
        "pandas",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "csv2db = csv2db.cli.main:cli",
        ],
    },
    python_requires=">=3.8.10",
)
