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

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String(100))
    body = db.Column(db.Text()) 
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body
        
    
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)



@app.route('/get/<court_query>', methods = ['GET'])
def get_specific_dining_court(court_query):
    article = Articles.query.filter_by(court=court_query)
    return article_schema.jsonify(article)


@app.route('/get', methods = ['GET'])
def get_articles():
    # return jsonify({"Hello": "World"})
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)


@app.route('/add', methods = ['POST'])
def add_article():
    data = json.loads(request.data)
    title = data['title']
    body = data['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)


@app.route('/update/<id>/', methods = ['PUT'])
def update_article(id):
    article = Articles.query.get(id)

    data = json.loads(request.data)
    title = data['title']
    body = data['body']

    article.title = title
    article.body = body

    db.session.commit()

    return article_schema.jsonify(article)

@app.route('/delete/<id>/', methods = ['DELETE'])
def article_delete(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()

    return article_schema.jsonify(article)


if __name__ == "__main__":
    app.run(debug=True)
