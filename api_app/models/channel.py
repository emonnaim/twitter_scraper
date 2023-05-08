from typing import TYPE_CHECKING,Optional
from datetime import datetime
from sqlmodel import Field,Relationship,SQLModel
if TYPE_CHECKING : 
    from .account import Account
    from .api import API
    from .blacklist_keyword import BlacklistKeyword
    from .whitelist_keyword import WhitelistKeyword
class Channel(SQLModel,table=True) : 
    id                  : Optional[int]  = Field(default=None, primary_key=True)
    name                : Optional[str]  = Field(default=None)
    channel_id          : Optional[int]  = Field(default=None)
    tweet_type          : Optional[str]  = Field(default=None)
    blacklist_check     : Optional[bool] = Field(default=None)
    replies_check       : Optional[bool] = Field(default=None)
    is_active           : Optional[bool] = Field(default=None)
    created_time        : datetime       = Field(default_factory=datetime.utcnow,nullable=False)
    ###### Relationships
    accounts            : list["Account"]          = Relationship(back_populates="channels")
    api_id              : Optional[int]            =  Field(default=None,foreign_key='api.id')
    api                 : Optional["API"]          = Relationship(back_populates="channels")
    blacklist_keywords  : list["BlacklistKeyword"] = Relationship(back_populates="channel")
    whitelist_keywords  : list["WhitelistKeyword"] = Relationship(back_populates="channel")