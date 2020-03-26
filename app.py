from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/katalog')
def katalog():
    return render_template('katalog.html')

@app.route('/rangliste')
def rangliste():
    return render_template('rangliste.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
