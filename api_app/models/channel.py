from typing import TYPE_CHECKING,Optional
from datetime import datetime
from sqlmodel import Field,Relationship,SQLModel
if TYPE_CHECKING : 
    from .account import Account
    from .api import API
    from .blacklist_keyword import BlacklistKeyword
    from .whitelist_keyword import WhitelistKeyword

class ChannelBase(SQLModel) : 
    name                : Optional[str]  
    channel_id          : Optional[int]  = Field(default=None)
    tweet_type          : Optional[str]  = Field(default=None)
    blacklist_check     : Optional[bool] = Field(default=None)
    replies_check       : Optional[bool] = Field(default=None)
    is_active           : Optional[bool] = Field(default=None)


class ChannelRead(ChannelBase) : 
    id : int
    pass 

class Channel(ChannelBase,table=True) : 
    id                  : Optional[int]  = Field(default=None, primary_key=True)
    created_time        : datetime   = Field(default_factory=datetime.utcnow,nullable=False)
    ###### Relationships
    accounts            : list["Account"]          = Relationship(back_populates="account_channel")
    api_id              : Optional[int]            =  Field(default=None,foreign_key='api.id')
    api                 : Optional["API"]          = Relationship(back_populates="channels")
    blacklist_keywords  : list["BlacklistKeyword"] = Relationship(back_populates="channel")
    whitelist_keywords  : list["WhitelistKeyword"] = Relationship(back_populates="channel")