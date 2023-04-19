from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

# session.py
from sqlalchemy.orm import sessionmaker
from engine import engine

Session = sessionmaker(bind=engine)
db = Session()