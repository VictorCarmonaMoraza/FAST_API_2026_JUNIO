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
```from fastapi import FastAPI

app = FastAPI(
    title="Biblioteca Personal API",
    description="API REST desarrollada con FastAPI",
    version="1.0.0"
)

@app.get("/")
def raiz():
    '''Endpoint básico que confirma que la API está funcionando.'''
    return {
        "mensaje": "La API de Biblioteca Personal está funcionando correctamente."
    }# Biblioteca Personal API
    
    API REST desarrollada con FastAPI siguiendo **Arquitectura Hexagonal**.
    
    ## Dependencias instaladas
    
    ```bash
    pip install fastapi "uvicorn[standard]" SQLAlchemy alembic python-dotenv PyMySQL cryptography
    ```
    
    | Paquete | Propósito |
    |---|---|
    | `fastapi` | Framework web para construir la API |
    | `uvicorn[standard]` | Servidor ASGI |
    | `SQLAlchemy` | ORM para base de datos |
    | `alembic` | Migraciones de base de datos |
    | `python-dotenv` | Carga de variables de entorno |
    | `PyMySQL` | Driver para MySQL |
    | `cryptography` | Utilidades criptográficas |
    
    ## Estructura del proyecto
    
    ```
    biblioteca_fastapi/
    ├── main.py
    ├── .env
    ├── requirements.txt
    ├── alembic.ini
    ├── alembic/
    │   └── versions/
    └── app/
        ├── domain/          # Núcleo — entidades, interfaces, excepciones
        ├── application/     # Casos de uso
        ├── infrastructure/  # Base de datos, configuración
        └── presentation/    # Routers FastAPI, schemas Pydantic
    ```
    
    ## Crear la estructura de carpetas
    
    ```powershell
    $files = @(
        "app/__init__.py",
        "app/domain/__init__.py",
        "app/domain/models/__init__.py",
        "app/domain/models/libro.py",
        "app/domain/repositories/__init__.py",
        "app/domain/repositories/libro_repository.py",
        "app/domain/exceptions/__init__.py",
        "app/domain/exceptions/libro_exceptions.py",
        "app/application/__init__.py",
        "app/application/services/__init__.py",
        "app/application/services/libro_service.py",
        "app/infrastructure/__init__.py",
        "app/infrastructure/config/__init__.py",
        "app/infrastructure/config/settings.py",
        "app/infrastructure/database/__init__.py",
        "app/infrastructure/database/connection.py",
        "app/infrastructure/database/models/__init__.py",
        "app/infrastructure/database/models/libro_orm.py",
        "app/infrastructure/database/repositories/__init__.py",
        "app/infrastructure/database/repositories/libro_repository_impl.py",
        "app/presentation/__init__.py",
        "app/presentation/schemas/__init__.py",
        "app/presentation/schemas/libro_schema.py",
        "app/presentation/api/__init__.py",
        "app/presentation/api/v1/__init__.py",
        "app/presentation/api/v1/router.py",
        "app/presentation/api/v1/endpoints/__init__.py",
        "app/presentation/api/v1/endpoints/libros.py"
    )
    
    foreach ($file in $files) {
        $dir = Split-Path $file
        if ($dir) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
        New-Item -ItemType File -Force -Path $file | Out-Null
    }
    
    Write-Host "Estructura creada correctamente."
    ```
    
    ## Levantar el servidor
    
    ```bash
    uvicorn main:app --reload
    ```