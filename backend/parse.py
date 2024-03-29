import json, datetime, random
from tokenize import Name
from unicodedata import name

def simplify_data(location, masterList):
    time = datetime.datetime.now()
    ftime = time.strftime("%m-%d-%Y")

    court = location
    fileOpen = open("backend/dataFiles/dining"+ location + ".json")
    diningData = json.load(fileOpen)
    for meal in diningData:
        mealTime = meal['Name']
        for station in meal['Stations']:
            for food in station['Items']:
                foodName = food['Name']
                rating = random.uniform(1.0, 5.0)
                rating = round(rating, 1)
                ratingsCount = random.uniform(1, 100)
                ratingsCount = round(ratingsCount)
                masterList.append(dict(date = ftime, court = court, food = foodName, meal_time = mealTime, ratings = rating, picture = "", ratings_count = ratingsCount))

    fileOpen.close()
    