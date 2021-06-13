from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/ms_main'
CORS(app)

db = SQLAlchemy(app)


class Dinosaur(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(128))
    image = db.Column(db.String(255))


@app.route('/')
def index():
    return 'Test'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
