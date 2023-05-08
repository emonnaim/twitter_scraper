from fastapi import FastAPI
from database import create_db_and_tables, engine
from models.account import Account
from models.tweet import Tweet
from models.api import API
from models.blacklist_keyword import BlacklistKeyword
from models.whitelist_keyword import WhitelistKeyword
from models.channel import Channel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, Session, SQLModel, select
from dependencies.database import get_session
from routers import accounts_router,apis_router,whitelist_keywords_router,blacklist_keywords_router,channels_router,apis_router

app = FastAPI()

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"],)
app.include_router(accounts_router.router)
app.include_router(apis_router.router)
app.include_router(whitelist_keywords_router.router)
app.include_router(blacklist_keywords_router.router)
app.include_router(channels_router.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=1996, log_level="info",reload=True)