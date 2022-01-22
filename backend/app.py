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

class DiningCourt(db.Model):
    id = db.Column(db.String(100), primary_key = True)

    date = db.Column(db.DateTime)
    court = db.Column(db.String(100))
    food = db.Column(db.String(100))
    meal_time = db.Column(db.String(100))
    ratings = db.Column(db.Float)
    picture = db.Column(db.String(100))

    def __init__(self, date, court, food, meal_time, ratings, picture):
        self.id = date + '.' + court + '.' + food
        self.date = datetime.datetime.strptime(date, "%m-%d-%Y")
        self.court = court
        self.food = food
        self.meal_time = meal_time
        self.ratings = ratings
        self.picture = picture
    
class DiningCourtSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'court', 'food', 'meal_time', 'ratings', 'picture')

dining_court_schema = DiningCourtSchema()
dining_courts_schema = DiningCourtSchema(many=True)



@app.route('/get/<court_query>', methods = ['GET'])
def get_specific_dining_court(court_query):
    all_dining = DiningCourt.query.filter_by(court=court_query)
    results = dining_courts_schema.dump(all_dining)
    return jsonify(results)

@app.route('/get/<id>', methods = ['GET'])
def get_specific_food(id):
    article = DiningCourt.query.get(id)
    return dining_court_schema.jsonify(article)


@app.route('/get', methods = ['GET'])
def get_all_food():
    all_dining = DiningCourt.query.all()
    results = dining_courts_schema.dump(all_dining)
    return jsonify(results)


@app.route('/add', methods = ['POST'])
def add_dining():
    data = json.loads(request.data)

    date = data['date']
    court = data['court']
    food = data['food']
    meal_time = data['meal_time']
    ratings = data['ratings']
    picture = data['picture']

    dining = DiningCourt(date, court, food, meal_time, ratings, picture)
    db.session.add(dining)
    db.session.commit()
    return dining_court_schema.jsonify(dining)


@app.route('/add_multi', methods = ['POST'])
def add_dining_multi():
    data_list = json.loads(request.data)

    for data in data_list:
        date = data['date']
        court = data['court']
        food = data['food']
        meal_time = data['meal_time']
        ratings = data['ratings']
        picture = data['picture']

        id = date + '.' + court + '.' + food
        if not DiningCourt.query.get(id):
            dining = DiningCourt(date, court, food, meal_time, ratings, picture)
            db.session.add(dining)
            db.session.commit()

    return jsonify({"Status": "OK"})


# @app.route('/update/<datetime>/', methods = ['PUT'])
# def update_article(datetime):
#     article = DiningCourt.query.get(datetime)

#     data = json.loads(request.data)
#     title = data['title']
#     body = data['body']

#     article.title = title
#     article.body = body

#     db.session.commit()

#     return dining_court_schema.jsonify(article)

# @app.route('/delete/<datetime>/', methods = ['DELETE'])
# def article_delete(datetime):
#     article = DiningCourt.query.get(datetime)
#     db.session.delete(article)
#     db.session.commit()

#     return dining_court_schema.jsonify(article)


if __name__ == "__main__":
    app.run(debug=True)
