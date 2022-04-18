"""A setuptools based setup module"""
import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="carga-reporte-final",
    version="0.2.0-beta",
    description="CLI para la carga del reporte final.csv a una base de datos Postgresql",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.agesic.gub.uy/data-science/ecosistema-covid/cdn-carga-reporte-final",
    author="Agesic",
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
            "carga_final = carga_reporte.cli.main:cli",
        ],
    },
    python_requires=">=3.8.10",
)
