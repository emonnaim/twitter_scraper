from dependencies.database import get_session,commit_changes
from models.blacklist_keyword import BlacklistKeyword
from sqlmodel import Field, Session, SQLModel, select
from fastapi import Depends, HTTPException, Query,status,Response,APIRouter

router = APIRouter(prefix="/blacklist_keywords",tags=["Blacklist Keywords"])

@router.get("")
def get_keywords(*,session : Session = Depends(get_session)) : 
    pass

@router.post('/{channel_id}')
def add_keywords_by_channel_id(*,channel_id : int,session : Session = Depends(get_session)) : 
    pass

@router.delete('/{channel_id}')
def delete_keywords_by_channel_id(*,channel_id : int,session : Session = Depends(get_session)) : 
    pass