import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import json

class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def getName(self):
        return self.name
    
    def updateName(self, name):
        self.name = name

    def getRating(self):
        return self.rating
    
    def updateRating(self, rating):
        self.rating = rating

    def printdata(self):
        print(self.name, self.rating)
    
p1 = Player("Noah Xu", 1922)