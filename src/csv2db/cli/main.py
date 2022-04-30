"""Modulo que implementa la CLI"""
import os
from datetime import date

import click
import numpy as np
import pandas as pd
from csv2db.models import Base
from sqlalchemy import create_engine

# Get cli directory path
basedir = os.path.abspath(os.path.dirname(__file__))


@click.group()
def cli() -> None:
    """Script to ingest csv file into a Postgresql database table"""
    pass


@click.command()
@click.option("-h", "--hostname", required=True, help="Database Host")
@click.option("-p", "--port", default=5432, help="Database Port", show_default=True)
@click.option("-d", "--database", required=True, help="Database Name")
@click.option("-u", "--username", required=True, help="Database Username")
@click.option("-w", "--password", required=True, help="Database Password")
def initdb(
    hostname: str, port: int, database: str, username: str, password: str
) -> None:
    """database initialization script"""
    try:
        click.echo("Initialized the database!")
        # database_url = "sqlite:///" + os.path.join(basedir, "database.db")
        database_url = (
            "postgresql+psycopg2://"
            + username
            + ":"
            + password
            + "@"
            + hostname
            + ":"
            + str(port)
            + "/"
            + database
        )
        engine = create_engine(database_url, echo=True, future=True)
        click.echo("Creating the ORM Model in the database")
        Base.metadata.create_all(engine)
    except Exception as exception:
        click.echo(exception)
    else:
        click.echo("Database Initialization Completed! :)")


@click.command(context_settings={"ignore_unknown_options": True})
@click.option("-h", "--hostname", required=True, help="Database Host")
@click.option("-p", "--port", default=5432, help="Database Port", show_default=True)
@click.option("-d", "--database", required=True, help="Database Name")
@click.option("-u", "--username", required=True, help="Database Username")
@click.option("-w", "--password", required=True, help="Database Password")
@click.argument(
    "file",
    type=click.Path(exists=True, file_okay=True, readable=True),
    required=True,
)
def loaddb(
    hostname: str,
    port: int,
    database: str,
    username: str,
    password: str,
    file: click.Path,
) -> None:
    """Load data from csv file to a PostgreSQL database table"""
    try:
        database_url = (
            "postgresql+psycopg2://"
            + username
            + ":"
            + password
            + "@"
            + hostname
            + ":"
            + str(port)
            + "/"
            + database
        )
        engine = create_engine(database_url, echo=True, future=True)
        click.echo("Loading data to the database")
        dataframe = pd.read_csv(
            file,
            skipfooter=1,
            keep_default_na=True,
            engine="python",
        ).fillna(0)
        dataframe["timestamp"] = date.today()

        casttype = {
            "franja": np.str0,
            "esp_dosis1": np.int64,
            "esp_dosis2": np.int64,
            "esp_dosis3": np.int64,
            "esp_dosis4": np.int64,
            "esp_dosis5": np.int64,
            "agen_dosis1": np.int64,
            "agen_dosis2": np.int64,
            "agen_dosis3": np.int64,
            "agen_dosis4": np.int64,
            "agen_dosis5": np.int64,
            "timestamp": np.datetime64,
        }
        dffinal = dataframe.iloc[:, 1:].astype(casttype)
        result = dffinal.to_sql("reportefinal", engine, if_exists="append", index=False)
    except Exception as exception:
        print(exception)
    else:
        click.echo(f"{result} rows were imported! :)")


cli.add_command(initdb)
cli.add_command(loaddb)

if __name__ == "__main__":
    cli()
