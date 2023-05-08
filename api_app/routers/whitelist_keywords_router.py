from dependencies.database import get_session,commit_changes
from models.whitelist_keyword import WhitelistKeyword
from sqlmodel import Field, Session, SQLModel, select
from fastapi import Depends, HTTPException, Query,status,Response,APIRouter

router = APIRouter(prefix="/whitelist_keywords",tags=["Whitelist Keywords"])

@router.get("")
def get_keywords(*,session : Session = Depends(get_session)) : 
    pass

@router.post('/{channel_id}')
def add_keywords_by_channel_id(*,channel_id : int,session : Session = Depends(get_session)) : 
    pass

@router.delete('/{channel_id}')
def delete_keywords_by_channel_id(*,channel_id : int,session : Session = Depends(get_session)) : 
    pass
