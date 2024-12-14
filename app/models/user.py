from app.commons.config import Base, session_factory
from sqlalchemy import Column, Integer, String
from flask import request

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(256), unique=True, nullable=False)
    email = Column('email', String(256), unique=True, nullable=False)
    password = Column('password', String(256))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
            
        }
        

def register_user():
    session = session_factory()
    user_data = request.get_json()
        
    name = user_data.get('name')
    email = user_data.get('email')
    password = user_data.get('password')

    try:
        new_user: User = User(name, email, password)
        session.add(new_user)
        session.commit()
        return new_user.to_json()
    except Exception as error:
        print(error)
        session.rollback()
        return error
    finally:
        session.close()


def get_all_users():
    session = session_factory()

    try:
        users: User = session.query(User).all()
        print(users)
        if users:          
            return {
                "items": [user.to_json() for user in users]
            }
        else: return {"message": 'User not found', "status": '404'}
    except Exception as error:
        print(error)
        return error
    finally:
        session.close()

def search_user(user_id):
    session = session_factory()

    try:
        user:User = session.query(User).get(user_id)
        if user:
            return user.to_json()
        else: return {"message": 'User not found', "status": '404'}
    except Exception as error:
        print(error)
        return error
    finally:
        session.close()

