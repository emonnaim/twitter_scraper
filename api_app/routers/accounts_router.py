from dependencies.database import get_session,commit_changes
from models.account import Account
from sqlmodel import Field, Session, SQLModel, select
from fastapi import Depends, HTTPException, Query,status,Response,APIRouter

router = APIRouter(prefix="/accounts",tags=["Accounts"])


@router.get("")
def get_accounts(*,session : Session = Depends(get_session)) : 
    pass

@router.get('/{channel_id}')
def get_accounts_by_group_Id(*,channel_id : int,session : Session = Depends(get_session)) : 
    pass

@router.post('/{channel_id}')
def add_accounts_to_channel_id(*,channel_id : int,session : Session = Depends(get_session)) : 
    pass

@router.delete('/{channel_id}')
def delete_accounts_by_channel_ids(*,channel_id : int,session : Session = Depends(get_session)) : 
    pass