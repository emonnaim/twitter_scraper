from typing import TYPE_CHECKING,Optional
from datetime import datetime
from sqlmodel import Field,Relationship,SQLModel
from sqlalchemy import Column,BigInteger
if TYPE_CHECKING : 
    from .account import Account
class Tweet(SQLModel,table=True) :
    id                  : Optional[int]  = Field(default=None, primary_key=True)
    tweet_id            : int            = Field(sa_column=Column(BigInteger))
    retweet_id          : int            = Field(sa_column=Column(BigInteger))
    tweet_username      : Optional[str]  = Field(default=None)
    tweet_status        : int            = Field(default=None)
    tweet_type          : Optional[str]  = Field(default=None)
    is_retweeted        : Optional[bool] = Field(default=None)
    content             : Optional[str]  = Field(default=None)
    media_url           : Optional[str]  = Field(default=None)
    created_time        : datetime   = Field(default_factory=datetime.utcnow,nullable=False)
    ### Relationships
    account_id : Optional[int] = Field(default=None, foreign_key="account.id")
    account : Optional["Account"] = Relationship(back_populates="tweets")


   