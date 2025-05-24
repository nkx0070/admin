from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a tu API con FastAPI!"}


@app.get("/health")
def read_root():
    return {"mensaje": "verificando estado de la app"}
