from typing import TYPE_CHECKING,Optional
from datetime import datetime
from sqlmodel import Field,Relationship,SQLModel
from sqlalchemy import BigInteger,Column
if TYPE_CHECKING : 
    from .channel import Channel
    from .tweet import Tweet

class Account(SQLModel,table=True) : 
    id            : Optional[int] = Field(default=None, primary_key=True)
    username      : str           = Field(unique=True)
    profile_pic   : Optional[str] = Field(default=None)
    last_tweet_id : Optional[int]          = Field(sa_column=Column(BigInteger))
    profile_pic   : Optional[str] = Field(default=None)
    filtered_tweets : Optional[int] = Field(default=None)
    sent_tweets     : Optional[int] = Field(default=None)
    muted_tweets    : Optional[int] = Field(default=None)
    created_time    : datetime   = Field(default_factory=datetime.utcnow,nullable=False)
    ##### Relationship
    channel_id      : Optional[int] =  Field(default=None,foreign_key='channel.id') 
    channel         : Optional["Channel"] = Relationship(back_populates="accounts")
    tweets          : list["Tweet"] = Relationship(back_populates="account")





