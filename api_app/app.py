from fastapi import FastAPI
from database import create_db_and_tables, engine
from models.account import Account
from models.tweet import Tweet
from models.api import API
from models.blacklist_keyword import BlacklistKeyword
from models.whitelist_keyword import WhitelistKeyword
from models.channel import Channel
import uvicorn
from sqlmodel import Field, Session, SQLModel, select
from dependencies.database import get_session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=1996, log_level="info")