import os
import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from producer import publish


app = Flask(__name__)
if os.getcwd() == '/app':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/ms_main'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:33007/ms_main'

CORS(app)

db = SQLAlchemy(app)


@dataclass
class Dinosaur(db.Model):
    id: int
    name: str
    image: str
    likes: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(128))
    image = db.Column(db.String(255))
    likes = db.Column(db.Integer, default=0)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'likes': self.likes
        }


@app.route('/api/dinosaur')
def index():
    return jsonify(Dinosaur.query.all())


@app.route('/api/like/<_id>')
def like(_id):
    dinosaur = Dinosaur.query.filter_by(id=int(_id)).first()
    dinosaur.likes += 1
    db.session.commit()
    publish('liked', dinosaur.to_json())
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
