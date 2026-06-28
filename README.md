# Biblioteca FastAPI

## Dependencias instaladas

Este proyecto usa las siguientes librerías base:

-   `fastapi`: framework web para construir APIs.
-   `uvicorn[standard]`: servidor ASGI para ejecutar FastAPI (con extras recomendados).
-   `SQLAlchemy`: ORM y manejo de base de datos.
-   `alembic`: migraciones de base de datos.
-   `python-dotenv`: carga de variables de entorno desde archivo `.env`.
-   `PyMySQL`: driver para conectar con MySQL desde Python.
-   `cryptography`: utilidades criptográficas (seguridad, cifrado, etc.).

## Instalación rápida

```bash
pip install fastapi "uvicorn[standard]" SQLAlchemy alembic python-dotenv PyMySQL cryptography
```