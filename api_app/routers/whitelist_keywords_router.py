from dependencies.database import get_session,commit_changes
from models.whitelist_keyword import WhitelistKeyword,KeywordRead
from models.channel import Channel
from sqlmodel import Field, Session, SQLModel, select
from fastapi import Depends, HTTPException, Query,status,Response,APIRouter

router = APIRouter(prefix="/whitelist_keywords",tags=["Whitelist Keywords"])

@router.get("/{channel_id}",response_model=list[KeywordRead])
def get_keywords(*,channel_id : int ,session : Session = Depends(get_session)) : 
    channel = session.get(Channel,channel_id)
    if channel == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Channel Not Found")
    return channel.whitelist_keywords

@router.post('/{channel_id}',response_model=list[KeywordRead])
def add_keywords_by_channel_id(keywords : list[str],channel_id : int,session : Session = Depends(get_session)) : 
    channel  =session.get(Channel, channel_id)
    print(channel)
    if channel == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Channel Not Found")
    for keyword in keywords : 
        channel.whitelist_keywords.append(WhitelistKeyword(keyword=keyword))
    commit_changes(session,[channel])
    session.refresh(channel)
    return channel.whitelist_keywords

@router.delete('/{channel_id}')
def delete_keywords_by_channel_id(keywords : list[str],channel_id : int,session : Session = Depends(get_session)) : 
    for keyword in keywords : 
        fetch_statement = select(WhitelistKeyword).where(WhitelistKeyword.keyword == keyword)
        keyword_object = session.exec(fetch_statement).first()
        if keyword_object == None : 
            continue
        session.delete(keyword_object)
        session.commit()
