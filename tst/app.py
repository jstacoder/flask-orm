from flask_orm import FlaskOrm
from sqlalchemy import Column, String
from flask import Flask

class User(FlaskOrm.Model):
    name = Column(String(255))

app = Flask(__name__)
app.config['DATABASE_URI'] = 'sqlite:///'
FlaskOrm(app)

@app.route('/')
def index():
    return User.query.filter(id=1).first().name
