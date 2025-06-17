from passlib.context import CryptContext
from jose import JWTError, jwt
from app.core.config import SECRET_KEY
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"

def hash_password(password:str) -> str:
    return pwd_context.hash(password)
def verify_password(password_txt:str, hashed_password:str)->str:
    return pwd_context.verify(password_txt,hashed_password)
#funciones tokens jwt
def create_acces_token(data:dict):

    data_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(data_encode,SECRET_KEY,algorithm = ALGORITHM)

    return encoded_jwt
def decode_acces_token(token:str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None