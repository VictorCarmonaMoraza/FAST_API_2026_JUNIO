from fastapi import FastAPI

# ==========================================================
# Creación de la aplicación FastAPI
# ----------------------------------------------------------
# La variable "app" representa la aplicación principal.
# Uvicorn buscará esta variable cuando iniciemos el servidor.
# ==========================================================

# Crear instancia principal de la apliacion FastApi
# 'app' sera utilizada por Uvicorn para levantar el servidor
app = FastAPI(
    title="Biblioteca Personal API",
    description="API REST desarrollada con FastAPI",
    version="1.0.0"
)

# Endpoint de prueba (ruta raiz)
# Sirve para verificar que la API esta viva
@app.get("/")
def raiz():
    '''
    Endpoint basica que confirma que la API esta funcionando
    '''
    return {
        "mensaje": "La API de Biblioteca Personal está funcionando correctamente."
    }