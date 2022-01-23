from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import json
import db_manage
import sqlite3

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class DiningCourtTimeline(db.Model):
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
    
class DiningCourtTimelineSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'court', 'food', 'meal_time', 'ratings', 'picture')

dining_court_timeline_schema = DiningCourtTimelineSchema()
dining_courts_timeline_schema = DiningCourtTimelineSchema(many=True)


@app.route('/get/<date_query>/<dining_court>', methods = ['GET'])
def get_specific_day_foodList(date_query, dining_court):
    date_query = datetime.datetime.strptime(date_query, "%m-%d-%Y")
    diningday = DiningCourtTimeline.query.filter_by(date=date_query, court=dining_court)

    reformatted_diningday = []
    for data_food in dining_courts_timeline_schema.dump(diningday):
        
        val = db_manage.populate_court_current_date(
            data_food['date'], data_food['court'], data_food['food'], data_food['meal_time']
        )
        
        reformatted_diningday.append(val)
            
    results = dining_courts_timeline_schema.dump(reformatted_diningday)

    return jsonify(results)

@app.route('/get/<date_query>/<dining_court>/top3', methods = ['GET'])
def get_specific_day_foodList_top3(date_query, dining_court):
    date_query = datetime.datetime.strptime(date_query, "%m-%d-%Y")
    diningday = DiningCourtTimeline.query.filter_by(date=date_query, court=dining_court)

    reformatted_diningday = []
    for data_food in dining_courts_timeline_schema.dump(diningday):
        
        val = db_manage.populate_court_current_date(
            data_food['date'], data_food['court'], data_food['food'], data_food['meal_time']
        )
        
        reformatted_diningday.append(val)

    reformatted_diningday = sorted(reformatted_diningday, key = lambda i: i['ratings'], reverse=True)[:3]
            
    results = dining_courts_timeline_schema.dump(reformatted_diningday)

    return jsonify(results)


@app.route('/get/<court_query>', methods = ['GET'])
def get_specific_dining_court(court_query):
    all_dining = DiningCourtTimeline.query.filter_by(court=court_query)
    results = dining_courts_timeline_schema.dump(all_dining)
    return jsonify(results)


@app.route('/get/<id>', methods = ['GET'])
def get_specific_food(id):
    article = DiningCourtTimeline.query.get(id)
    return dining_court_timeline_schema.jsonify(article)


@app.route('/get', methods = ['GET'])
def get_all_food():
    all_dining = DiningCourtTimeline.query.all()
    results = dining_courts_timeline_schema.dump(all_dining)
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

    dining = DiningCourtTimeline(date, court, food, meal_time, ratings, picture)
    db.session.add(dining)
    db.session.commit()
    return dining_court_timeline_schema.jsonify(dining)


@app.route('/add_multi', methods = ['POST'])
def add_dining_multi():
    data_list = json.loads(request.data)

    for data in data_list:
        date = data['date']
        court = "".join([i.lower() for i in data['court'].split()])
        food = "".join([i for i in data['food'].split()])     
        meal_time = data['meal_time']
        ratings = data['ratings']
        picture = data['picture']

        id = date + '.' + court + '.' + food
        if not DiningCourtTimeline.query.get(id):
            dining = DiningCourtTimeline(date, court, food, meal_time, ratings, picture)
            db.session.add(dining)
            db.session.commit()

    return jsonify({"Status": "OK"})

@app.route('/add_dining_ratings', methods = ['POST'])
def add_dining_ratings():
    f = open('backend/dataFiles/dining_01-22-2022PRO.json')
    loaded_data = json.load(f)

    count = 0
    for val in loaded_data:
        # print(val)
        # if count == 10:
        #     break
        court = "".join([i.lower() for i in val['court'].split()])
        foodid = "".join([i for i in val['food'].split()])        
        foodori = val['food']
        db_manage.populate_db_ratings(
            court,
            foodid,
            foodori,
            val['ratings'],
            val.get('ratings_count', 0.0),
            val['picture']
        )
        count += 1

    return jsonify({"Status": "OK"})

@app.route('/update_ratings', methods = ['POST'])
def update_dining_ratings():
    # Sample data
    # {
    #     "date": "01-22-2022",
    #     "court": "Wiley",
    #     "food": "Scrambled Eggs",
    #     "meal_time": "Breakfast",
    #     "ratings": 4.3,
    #     "picture": "",
    #     "ratings_count": 11
    # }

    val = json.loads(request.data)
    
    if not val:
        return jsonify({"Status": "No data"})

    court = "".join([i.lower() for i in val['court'].split()])
    food = "".join([i for i in val['food'].split()]) 

    val = db_manage.update_ratings(court, food, val['ratings'])

    return dining_court_timeline_schema.jsonify(val)


# @app.route('/update/<datetime>/', methods = ['PUT'])
# def update_article(datetime):
#     article = DiningCourtTimeline.query.get(datetime)

#     data = json.loads(request.data)
#     title = data['title']
#     body = data['body']

#     article.title = title
#     article.body = body

#     db.session.commit()

#     return dining_court_timeline_schema.jsonify(article)

# @app.route('/delete/<datetime>/', methods = ['DELETE'])
# def article_delete(datetime):
#     article = DiningCourtTimeline.query.get(datetime)
#     db.session.delete(article)
#     db.session.commit()

#     return dining_court_timeline_schema.jsonify(article)


if __name__ == "__main__":
    app.run(debug=True)
