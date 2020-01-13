from datetime import *

class Day:

    def __init__(self, time_distance):
        self.activities = None
        self.percent    = None
        self.mood       = None
        self.date       = date.today() + timedelta(days = time_distance)


