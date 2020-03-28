from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    modul = Column(String(100), nullable=False)
    question = Column(String(250), nullable=False)
    solution = Column(String(250), nullable=False)



engine = create_engine('sqlite:///questionaire.db')
Base.metadata.create_all(engine)