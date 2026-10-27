"""FastAPI-приложение «Hello»."""
from fastapi import FastAPI

app = FastAPI(title="FastAPI Hello")

@app.get("/")
def hello() -> dict:
    """Возвращает приветствие в JSON."""
    return {"message": "Привет FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)