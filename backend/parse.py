import json

fileOpen = open(dining.json)

diningData = json.load(fileOpen)

for foodItem in diningData['emp_details']:
    print(foodItem)

fileOpen.close()