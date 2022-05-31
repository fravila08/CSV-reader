from calendar import c
import csv
import os
dogs=[]
cats=[]
class Pets: 
    def __init__(self, name, age, breed):
        self.name=name
        self.age=age
        self.breed=breed
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed}."

question=input('Choose between cats or dogs:')
question=question.lower()
if question=='cats':
    with open(os.getcwd()+'/data/cats.csv', newline='') as csvfile:
        spamreader=csv.reader(csvfile,delimiter=' ', quotechar='|')
        for row in spamreader:
            cats.append(Pets(row[0],row[1],row[2]))
    cats.pop(0)
    for i in cats:
        print(i)
if question=='dogs':
    with open(os.getcwd()+'/data/dogs.csv', newline='') as csvfile:
        spamreader=csv.reader(csvfile,delimiter=' ', quotechar='|')
        for row in spamreader:
            dogs.append(Pets(row[0],row[1],row[2]))
    dogs.pop(0)
    for i in dogs:
        print(i)
else:
    print('Sorry, don\'t have any birds here')