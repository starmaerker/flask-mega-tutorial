class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    modul = Column(String(100), nullable=False)
    question = Column(String(250), nullable=False)
    solution = Column(String(250), nullable=False)
