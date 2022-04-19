# CLI - Ingesta de Reporte final.csv a base Postgresql

---

Paquete Python que implementa una **CLI** para automatizar la ingesta o carga del archivo **final.csv** hacia una base de Datos Postgresql.

## ¿Cómo instalar el paquete?

- Crear un entorno virtual (virtual environment) de Python `python -m venv venv`
- Track 1
  - Descargar el presente código desde el VCS (gitlab) a una carpeta local
  - Activar el entorno virtual y ejecutar el comando `python -m pip install .`
- Track 2
  - Instalarlo directamente desde el VCS `python -m pip install git+https://gitlab.agesic.gub.uy/data-science/ecosistema-covid/cdn-carga-reporte-final.git`

> El script **python** utilizado en los tracks 1 y 2 debe de ser el instalado en el entorno virtual y no el genérico de la instación del sistema operativo.

## Modo de uso

Una vez instalado el paquete solamente tenemos que ejecutar el script:

```bash
Usage: carga_final [OPTIONS] COMMAND [ARGS]...

  Script to ingest final.csv report into a Postgresql database

Options:
  --help  Show this message and exit.

Commands:
  initdb  database initialization script
  loaddb  Load data from final.csv file to database

```

### Comando para la inicialización de la Base de Datos

```bash
Usage: carga_final initdb [OPTIONS]

  database initialization script

Options:
  -h, --hostname TEXT  Database Host  [required]
  -p, --port INTEGER   Database Port  [default: 5432]
  -d, --database TEXT  Database Name  [required]
  -u, --username TEXT  Database Username  [required]
  -w, --password TEXT  Database Password  [required]
  --help               Show this message and exit.

```

### Comando para la ingesta del reporte a la Base de Datos

```bash
Usage: carga_final loaddb [OPTIONS] FILE

  Load data from final.csv file to database

Options:
  -h, --hostname TEXT  Database Host  [required]
  -p, --port INTEGER   Database Port  [default: 5432]
  -d, --database TEXT  Database Name  [required]
  -u, --username TEXT  Database Username  [required]
  -w, --password TEXT  Database Password  [required]
  --help               Show this message and exit.
```
