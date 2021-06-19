from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from dataclasses import dataclass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/ms_main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Dinosaur(db.Model):
    id: int
    name: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(128))
    image = db.Column(db.String(255))


@app.route('/api/dinosaur')
def index():
    return jsonify(Dinosaur.query.all())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
