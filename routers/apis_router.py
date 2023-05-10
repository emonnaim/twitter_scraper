from dependencies.database import get_session,commit_changes
from models.api import API,APICreate,APIRead
from models.channel import Channel
from sqlmodel import Field, Session, SQLModel, select
from fastapi import Depends, HTTPException, Query,status,Response,APIRouter

router = APIRouter(prefix="/apis",tags=["API"])

@router.get("",response_model=list[APIRead])
def get_apis(*,session : Session = Depends(get_session)) :
    fetch_statement = select(API)
    apis = session.exec(fetch_statement).all()
    return apis

@router.post('',response_model=APIRead)
def add_api(api : APICreate,session : Session = Depends(get_session)) : 
    try : 
        api  = API.from_orm(api)
        commit_changes(session,[api])
        return api
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail=e)


@router.delete('/{api_id}')
def delete_api(api_id : int,session : Session = Depends(get_session)) : 

    api =  session.get(API,api_id)
    if api == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="API Not Found")
    session.delete(api)
    session.commit()
    
@router.post('/select_api/{channel_id}')
def select_api(api_id : int , channel_id: int,session : Session = Depends(get_session)) : 
    api = session.get(API,api_id)
    channel = session.get(Channel,channel_id)
    if api == None or channel == None : 
        raise HTTPException(status_code=404,detail='Either channel or api not found')
    channel.api = api
    commit_changes(session=session,changes=[channel])
