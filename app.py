from flask import Flask
from flask import render_template, url_for
from forms import CreateQuestion
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/katalog')
def katalog():
    return render_template('katalog.html')

@app.route('/create')
def create():
    form = CreateQuestion()
    return render_template('create.html', form=form)

@app.route('/rangliste')
def rangliste():
    return render_template('rangliste.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()

import models