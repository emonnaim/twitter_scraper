from dependencies.database import get_session,commit_changes
from models.account import Account,AccountRead
from models.channel import Channel
from sqlmodel import Field, Session, SQLModel, select
from fastapi import Depends, HTTPException, Query,status,Response,APIRouter

router = APIRouter(prefix="/accounts",tags=["Accounts"])


@router.get("",response_model=list[AccountRead])

def get_accounts(session : Session = Depends(get_session)) : 
    fetch_statement = select(Account)
    accounts = session.exec(fetch_statement).all()
    print(accounts)
    return accounts

@router.get('/{channel_id}',response_model=list[Account])
def get_accounts_by_channel_Id(channel_id : int,session : Session = Depends(get_session)) : 
    try : 
        return session.get(Channel,channel_id).accounts
    except Exception as e : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Channel Not Found")


@router.post('/{channel_id}',response_model=list[Account])
def add_accounts_to_channel_id(channel_id : int,usernames : list[str] ,session : Session = Depends(get_session)) : 
    channel = session.get(Channel,channel_id)
    if channel == None : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Channel Not Found")
    else : 
        for username in usernames : 
            try : 
                account = session.exec(select(Account).where(Account.username == username)).first()
                if account : 
                    continue
                account = Account(username=username,account_channel=channel)
                commit_changes(session,[account])
                session.refresh(channel)
            except Exception as e : 
                pass
        return channel.accounts
@router.delete('/{channel_id}',response_model=list[Account])
def delete_accounts_by_channel_ids(channel_id : int,usernames : list[str],session : Session = Depends(get_session)) : 
    for username in usernames : 
        try : 
            account = session.exec(select(Account).where(Account.username == username)).first()
            session.delete(account)
            session.commit()
        except Exception as e : 
            pass
    return session.get(Channel,channel_id).accounts
