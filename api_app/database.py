from sqlmodel import SQLModel, create_engine
from config import *

postgres_url = f"{db_type}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(postgres_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)