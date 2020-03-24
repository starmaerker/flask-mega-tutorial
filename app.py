from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/katalog')
def katalog():
    return 'katalog'

@app.route('/rangliste')
def rangliste():
    return 'Rangliste'

@app.route('/login')
def login():
    return 'Login'


if __name__ == '__main__':
    app.run()
