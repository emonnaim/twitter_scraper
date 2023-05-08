from dependencies.database import get_session,commit_changes
from models.api import API
from sqlmodel import Field, Session, SQLModel, select
from fastapi import Depends, HTTPException, Query,status,Response,APIRouter

router = APIRouter(prefix="/apis",tags=["API"])

@router.get("")
def get_apis(*,session : Session = Depends(get_session)) : 
    pass

@router.post('/{channel_id}')
def add_api(channel_id : int,session : Session = Depends(get_session)) : 
    pass

@router.delete('/{api_id}')
def delete_api(api_id : int,session : Session = Depends(get_session)) : 
    pass