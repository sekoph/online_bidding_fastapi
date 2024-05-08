from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.security import OAuth2AuthorizationCodeBearer , OAuth2PasswordRequestForm

from schemas.user import CreateUser
from models.user import User





# select user by id
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# get users by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# get all users
def get_users(db: Session, skip: int, limit: int):
    return db.query(User).offset(skip).limit(limit).all()


# create users
def Create_User(db: Session, user: CreateUser):
    try:
        new_user = User(username = user.username, email = user.email, hashed_password = user.password, role = user.role)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        return False


