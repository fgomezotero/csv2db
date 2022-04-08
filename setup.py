from setuptools import find_packages, setup

setup(
    name="carga-reporte-final",
    version="0.1.0",
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
            "load_final = carga_reporte.cli.main:cli",
        ],
    },
    python_requires=">=3.8",
)
