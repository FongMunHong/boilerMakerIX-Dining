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
        fields = ('id', 'court', 'food', 'ratings', 'ratings_count', 'picture')


dining_court_rating_schema = DiningRatingHistSchema()
dining_courts_rating_schema = DiningRatingHistSchema(many=True)

def populate_court_current_date(date, court, food, meal_time):

    id = court + "." + food
    foodRatings = DiningRatingHist.query.get(id)
    foodRatings = dining_court_rating_schema.dump(foodRatings)

    if foodRatings:
        foodRatings = {
            "date": date,
            "meal_time": meal_time,
            **foodRatings
        }
        del foodRatings['id']
    else:
        # foodRatings = DiningRatingHist()
        foodRatings = {
            "date": date,
            "meal_time": meal_time,
            "court": court,
            "food": food,
            "ratings": 0.0,
            "ratings_count": 0,
            "picture": ""
        }

    return foodRatings


def populate_db_ratings(court, food, ratings, ratings_count, picture):
    
    id = court + '.' + food
    if not DiningRatingHist.query.get(id):
        diningRating = DiningRatingHist(court, food, ratings, ratings_count, picture)
        db.session.add(diningRating)
        db.session.commit()

    return

def update_ratings(court, food, ratings):

    id = court + '.' + food
    if DiningRatingHist.query.get(id):
        diningFood = DiningRatingHist.query.get(id)
        temp_ratings_count = diningFood.ratings_count
        
        print (diningFood.ratings * temp_ratings_count)
        

        avg_ratings = ((diningFood.ratings * temp_ratings_count) + ratings) / (temp_ratings_count + 1)
        diningFood.ratings = round(avg_ratings, 1)
        diningFood.ratings_count += 1

        db.session.commit()

        return diningFood



if __name__ == "__main__":
    app.run(debug=True)
