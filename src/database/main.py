from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import database_config

database_name = database_config.DATABASE_NAME
database_username = database_config.DATABASE_USERNAME
database_password = database_config.DATABASE_PASSWORD

db_url = f"postgresql://{database_username}:{database_password}@localhost:5432/{database_name}"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, bind=engine)


def get_db():
    """
    Dependency function for providing a SQLAlchemy database session.

    This function creates a new session to the database and ensures it is
    properly closed after use. It is designed to be used with FastAPI's
    `Depends` in path operations.

    Yields:
        Session: A SQLAlchemy database session that can be used to query
        and persist data.
    """
    db = session()
    try:
        yield db
    finally:
        db.close()
