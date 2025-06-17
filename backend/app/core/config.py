import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "")
SECRET_KEY = os.getenv("SECRET_KEY","")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY no está definida. Verificá el archivo .env")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definida. Verificá el archivo .env")
