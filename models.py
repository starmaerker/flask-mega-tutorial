from app import db


class Question(db.Model):
    # to choose own table name at attribute __tablename__
    id = db.Column(db.Integer, primary_key=True)
    modul = db.Column(db.String(100), nullable=False)
    question = db.Column(db.String(250), nullable=False, unique=True)
    solution = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Question {} aus Modul {}>'.format(self.question, self.modul)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
