from dependencies.database import get_session,commit_changes
from models.account import Account
from models.channel import Channel,ChannelRead
from sqlmodel import Field, Session, SQLModel, select
from fastapi import Depends, HTTPException, Query,status,Response,APIRouter

router = APIRouter(prefix="/channels",tags=["Channels"])

@router.get("",response_model=list[ChannelRead])
def get_channels(*,session : Session = Depends(get_session)) : 
    fetch_statement = select(Channel)
    channels = session.exec(fetch_statement).all()
    return channels

@router.post('/add_channel',response_model=ChannelRead)
def add_channel(*,channel_name : str,session : Session = Depends(get_session)) : 
    try : 
        channel = Channel(name=channel_name)
        commit_changes(session=session,changes=[channel])
        return channel
    except Exception as e : 
        raise HTTPException(status_code=status.WS_1011_INTERNAL_ERROR,detail=e)
@router.delete('/delete_channel/{channel_id}')
def delete_channel(*,channel_id : int,session : Session = Depends(get_session)) : 
    try :
        channel = session.get(Channel,channel_id)
        session.delete(channel)
        session.commit()
    except Exception as e : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=e)

@router.post('/channel_status/{channel_id}')
def change_channel_status(status  : bool ,channel_id : int,session : Session = Depends(get_session)) : 

    channel = session.get(Channel,channel_id)
    if channel == None : 
        raise HTTPException(status_code=404,detail="Channel Not Found")
    channel.is_active = status
    commit_changes(session,[channel])
    
@router.post('/replies_statues/{channel_id}')
def change_replies_status(status  : bool ,channel_id : int,session : Session = Depends(get_session)) : 

    channel = session.get(Channel,channel_id)
    if channel == None : 
        raise HTTPException(status_code=404,detail="Channel Not Found")
    channel.replies_check = status
    commit_changes(session,[channel])

@router.post('/blacklist_statues/{channel_id}')
def change_replies_status(status  : bool ,channel_id : int,session : Session = Depends(get_session)) : 

    channel = session.get(Channel,channel_id)
    if channel == None : 
        raise HTTPException(status_code=404,detail="Channel Not Found")
    channel.blacklist_check = status
    commit_changes(session,[channel])

@router.post('/tweet_type/{channel_id}')
def change_tweet_type(tweet_type : str ,channel_id : int,session : Session = Depends(get_session)) : 

    channel = session.get(Channel,channel_id)
    if channel == None : 
        raise HTTPException(status_code=404,detail="Channel Not Found")
    channel.tweet_type = tweet_type
    commit_changes(session,[channel])
