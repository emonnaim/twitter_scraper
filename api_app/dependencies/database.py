from sqlmodel import  Session
from database import engine

def get_session():
    with Session(engine) as session:
        yield session

def commit_changes(session : Session, changes : list) : 
    try : 
        session.add_all(changes)
        session.commit()
        #session.refresh(changes)
    except Exception as e : 
        print("error in commit")
        print(e)