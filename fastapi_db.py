"""FastAPI с базой данных SQLite через SQLAlchemy."""
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

app = FastAPI(title="FastAPI with DB")
Base = declarative_base()

class User(Base):
    """Модель пользователя."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

engine = create_engine("sqlite:///fastapi_demo.db", echo=False)
Base.metadata.create_all(engine)

@app.get("/users")
def get_users() -> list[dict]:
    """Возвращает всех пользователей."""
    with Session(engine) as session:
        users = session.query(User).all()
        return [{"id": u.id, "name": u.name} for u in users]

@app.post("/users")
def create_user(name: str) -> dict:
    """Создаёт пользователя по имени."""
    with Session(engine) as session:
        user = User(name=name)
        session.add(user)
        session.commit()
        return {"id": user.id, "name": user.name}

@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict:
    """Возвращает пользователя по id."""
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {"id": user.id, "name": user.name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)