from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, UserLogin, TokenOut
from app.core.security import verify_password, create_acces_token,decode_acces_token
from app.services.users import create_user, get_current_user
from app.services.db import get_db
from app.db.models import User
from app.core.security import oauth2_scheme

router = APIRouter()

  # para manejar el token

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)): #se asegura de tener una session
    return create_user(db, user)
@router.post("/login", response_model=TokenOut)
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_login.email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    if not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    
    token = create_acces_token({"sub": user.email})

    return {"access_token": token, "token_type": "bearer"}

@router.get("/mytasks", response_model=UserOut)
def my_tasks(user: User = Depends(get_current_user)):
    return user