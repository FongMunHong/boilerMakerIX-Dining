import json, datetime, random
from tokenize import Name
from unicodedata import name

fileOpen = open("dining.json")

diningData = json.load(fileOpen)

time = datetime.datetime.now()
ftime = time.strftime("%m-%d-%Y")

listOfDicts = []
#Wiley

court = "Wiley"
for meal in diningData:
    mealTime = meal['Name']
    for station in meal['Stations']:
        for food in station['Items']:
            foodName = food['Name']
            rating = random.uniform(1.0, 5.0)
            rating = round(rating, 1)
            listOfDicts.append(dict(datetime = ftime, court = court, food = foodName, mealtime = mealTime, ratings = rating, picture = ""))
            

with open("newFormat.json", "w") as outfile:
    json.dump(listOfDicts, outfile)            



fileOpen.close()