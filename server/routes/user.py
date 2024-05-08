from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import SessionLocal
from crud.user import Create_User, get_users,get_user_by_email
from schemas.user import User, CreateUser


usersRouter = APIRouter()

# define database dependancy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        



# create new user
@usersRouter.post('/users/', response_model = User)
def create_user( new_user: CreateUser, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db = db , email = new_user.email)
    if db_user:
        raise HTTPException(status_code = 400, detail="email exists")
    return Create_User(db = db, user = new_user)


# get all users
@usersRouter.get('/user/', response_model = list[User])
def users(skip : int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip = skip, limit = limit)


# get user by email
@usersRouter.get('/users/{email}', response_model = User)
def get_user(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db = db , email = email)
    if user is None:
        raise HTTPException(status_code= 404, detail="user does not exist")
    return user
