from datetime import date, timedelta

class Day:

    def __init__(self, time_distance):
        self.activities = None
        self.percent    = None
        self.mood       = None
        self.date       = datetime.today() + timedelta(days = time_distance)


