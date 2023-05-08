from dependencies.database import get_session,commit_changes
from models.account import Account
from sqlmodel import Field, Session, SQLModel, select
from fastapi import Depends, HTTPException, Query,status,Response,APIRouter

router = APIRouter(prefix="/channels",tags=["Channels"])

@router.get("")
def get_channels(*,session : Session = Depends(get_session)) : 
    pass

@router.post('/{channel_id}')
def add_channel(*,channel_id : int,session : Session = Depends(get_session)) : 
    pass

@router.delete('/{channel_id}')
def delete_channel(*,channel_id : int,session : Session = Depends(get_session)) : 
    pass