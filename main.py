#import json file
import json

#did file work?
a = open('animals.json')
data = json.load(a)

for i in data['livestock']:
  print(i)

#sort
from itertools import groupby
from operator import itemgetter

livestock = [
        {"animal": "Goat", "barn": "Green"},
        {"animal": "Rabbit", "barn": "Blue"},
        {"animal": "Cow", "barn": "Red"},
        {"animal": "Calf", "barn": "Black"},
        {"animal": "Donkey", "barn": "Brown"},
        {"animal": "Duck", "barn": "Green"},
        {"animal": "Chicken", "barn": "Blue"},
        {"animal": "Pig", "barn": "Red"},
        {"animal": "Cat", "barn": "Black"},
        {"animal": "Dog", "barn": "Brown"},
        {"animal": "Chicken", "barn": "Green"},
        {"animal": "Duck", "barn": "Blue"},
        {"animal": "Rabbit", "barn": "Red"},
        {"animal": "Goat", "barn": "Black"},
        {"animal": "Rooster", "barn": "Brown"},
        {"animal": "Pig", "barn": "Green"},
        {"animal": "Horse", "barn": "Blue"},
        {"animal": "Donkey", "barn": "Red"},
        {"animal": "Cat", "barn": "Black"},
        {"animal": "Dog", "barn": "Brown"},
        {"animal": "Goat", "barn": "Red"},
        {"animal": "Pig", "barn": "Red"},
        {"animal": "Chicken", "barn": "Red"},
        {"animal": "Duck", "barn": "Red"},
        {"animal": "Cat", "barn": "Red"}
    ]

# Sort animals data by barn color key.
livestock = sorted(livestock, key = itemgetter('barn'))
  
# Display barns grouped by barn color
for key, value in groupby(livestock,key = itemgetter('barn')):
    print(key)
    for k in value:
        print(k)
