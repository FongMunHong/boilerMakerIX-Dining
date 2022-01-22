from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import json
import sqlite3

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class DiningRatingHist(db.Model):
    id = db.Column(db.String(100), primary_key = True)

    court = db.Column(db.String(100))
    food = db.Column(db.String(100))
    ratings = db.Column(db.Float)
    ratings_count = db.Column(db.Integer)
    picture = db.Column(db.String(100))

    def __init__(self, court, food, ratings, ratings_count, picture):
        self.id = court + '.' + food
        self.court = court
        self.food = food
        self.ratings = ratings
        self.ratings_count = ratings_count
        self.picture = picture
    
class DiningRatingHistSchema(ma.Schema):
    class Meta:
        fields = ('id', 'court', 'food', 'ratings', 'ratings_count')

def populate_court_current_date(date, court, meal_time, foodList):
    listOfFood = []
    for food in foodList:
        id = court + "." + food
        foodRatings = DiningRatingHist.query.get(id)
        foodRatings = {
            "date": date,
            "meal_time": meal_time
            **foodRatings
        }
        listOfFood.append(foodRatings)

    return listOfFood



if __name__ == "__main__":
    app.run(debug=True)
