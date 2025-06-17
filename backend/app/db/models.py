from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)#integer PK por defecto se convierte en valor SERIAL
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="employee")
    #permite consultas como ticket.user.tkt_num como FK pero con objetos:
    tickets = relationship("Tickets", back_populates="user")
class Tickets(Base):
    __tablename__ = "tickets"

    tkt_num = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    description = Column(String, default="Ticket Description")
    user_id = Column(Integer, ForeignKey("users.id"))
    typ = Column(String,default = "tech")
    user = relationship("User", back_populates="tickets")  

