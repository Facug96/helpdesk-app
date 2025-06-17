from sqlalchemy.orm import Session
from app.db.models import User
from app.core.security import hash_password,decode_acces_token 
from fastapi import Depends, HTTPException
from jose import JWTError
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user import UserCreate
from app.services.db import get_db
from app.core.security import oauth2_scheme



def create_user(db: Session, user_data: UserCreate):
    hashed_pw = hash_password(user_data.password)
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_pw,
        role=user_data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_acces_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Token inválido")

    email = payload.get("sub")
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return user