
from typing import TYPE_CHECKING,Optional
from datetime import datetime
from sqlmodel import Field,Relationship,SQLModel
if TYPE_CHECKING : 
    from .channel import Channel

class BlacklistKeyword(SQLModel,table=True):
    id                  : Optional[int]  = Field(default=None, primary_key=True)
    keyword            : Optional[str]  = Field(default=None)
    created_time        : datetime   = Field(default_factory=datetime.utcnow,nullable=False)
    #### Relationship
    channel_id : Optional[int] = Field(default=None,foreign_key="channel.id")
    channel : Optional["Channel"] = Relationship(back_populates="blacklist_keywords")

