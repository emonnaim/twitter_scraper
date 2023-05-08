from typing import TYPE_CHECKING,Optional
from datetime import datetime
from sqlmodel import Field,Relationship,SQLModel
if TYPE_CHECKING : 
    from .channel import Channel
class API(SQLModel,table=True) :
    id                  : Optional[int]  = Field(default=None, primary_key=True)
    name                : Optional[str]  = Field(default=None)
    api_key             : Optional[str]  = Field(default=None)
    api_secret          : Optional[str]  = Field(default=None)
    created_time        : datetime   = Field(default_factory=datetime.utcnow,nullable=False)
    #### Relationships
    channels : list["Channel"] = Relationship(back_populates="api")




