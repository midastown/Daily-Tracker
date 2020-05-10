from datetime import date, timedelta
from mood import *

class Day:

    def __init__(self, time_distance):
        self.activities = None
        self.mood       = Mood() 
        self.percentage = None
        self.metrics    = {}
        self.date       = date.today() + timedelta(days = time_distance)

