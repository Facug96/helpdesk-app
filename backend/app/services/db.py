from app.db.database import SessionLocal


def get_db(): #para tocar la db necesito session
    db = SessionLocal() #definido en db.database
    try:
        yield db
    finally:
        db.close()