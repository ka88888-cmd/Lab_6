"""Демонстрация подключения SQLAlchemy к SQLite."""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class User(Base):
    """Модель пользователя."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

engine = create_engine("sqlite:///sqlalchemy_demo.db", echo=False)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    with Session(engine) as session:
        session.add(User(name="Екатерина"))
        session.commit()
        users = session.query(User).all()
        print([u.name for u in users])