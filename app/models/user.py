from app.commons.config import Base, session_factory
from app.commons.dtos import validation
from sqlalchemy import Column, Integer, String
from http import HTTPStatus
from flask import request
import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(256), nullable=False)
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

        

def register_user(user_data):
    if not user_data or not user_data.get('name') or not user_data.get('password') or not user_data.get('email'):
        return {'message': 'insufficient data'}, HTTPStatus.BAD_REQUEST
        
    error, result = validation(user_data) 
    if result == HTTPStatus.UNPROCESSABLE_ENTITY:
        return {'message': error}, HTTPStatus.UNPROCESSABLE_ENTITY

    name = user_data.get('name')
    email = user_data.get('email')
    password = user_data.get('password')

    session = session_factory()
    try:
        new_user: User = User(name, email, password)
        session.add(new_user)
        session.commit()
        return new_user.to_json(), HTTPStatus.CREATED
    except Exception as error:
        print(error)
        session.rollback()
        return {'message': str(error)}, HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()
        

def get_all_users():
    session = session_factory()

    try:
        users: User = session.query(User).all()
        print(users)
        if users:          
            return {"items": [user.to_json() for user in users]}, HTTPStatus.OK
        else: 
            return {'message': "User not found"} , HTTPStatus.NOT_FOUND
        
    except Exception as error:
        print(error)
        session.rollback()
        return {'message': error}, HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

def search_user(user_info):
    session = session_factory()

    try:
        user: User = session.query(User).filter(User.id == user_info).first()
        if user:
            print(user)
            return user.to_json(), HTTPStatus.OK
        user: User = session.query(User).filter(User.email == user_info).first()
        if user:
            print(user)
            return user.to_json(), HTTPStatus.OK
        else: 
            return {"message": 'User not found'}, HTTPStatus.NOT_FOUND
    except Exception as error:
        print(error)
        session.rollback()
        return {'message': error}, HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

def update_user(user_id, user_data: dict):
    session = session_factory()

    try:
        if not user_data:
            return {'message': 'insufficient data'}, HTTPStatus.BAD_REQUEST

        alterd_row = session.query(User).filter(User.id == user_id).update({
            User.email: user_data['email'],
            User.name: user_data['name'],
            User.password: user_data['password']
        })
        if alterd_row == 0:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        session.commit()
        return user_data, HTTPStatus.OK
    except Exception as error:
        print(error)
        session.rollback()
        return {'message': error}, HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()

def delete_user(user_id):
    session = session_factory()
    try:
        user: User = session.query(User).filter(User.id == user_id).first()
        if not user:
            return {'message': 'user not found or already deleted'}, HTTPStatus.NOT_FOUND
        session.delete(user)
        session.commit()
        return {'message': 'user deleted'}, HTTPStatus.NO_CONTENT
    except Exception as error:
        print(error)
        session.rollback()
        return {'message': error}, HTTPStatus.INTERNAL_SERVER_ERROR
    finally:
        session.close()
    

