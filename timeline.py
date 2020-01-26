from day import *
from datetime import date

class Timeline:

    def __init__(self):
        self.timeline = {}
        self.week = 1
        

    def add_week(self):
        """
        Creates a new instance of a week and store it into the timeline
        Returns nothing.
        """
        week = []
        if not self.timeline:
            # if its the first week
            distance = 0
        else:
            today = date.today()
            # basically the math is (difference between the last day in timeline and today) + 1 for the next day
            distance = (self.timeline["week"+str(self.week-1)][-1].date - today).days + 1

            
        for i in range(7):
            day = Day(distance)                                      # instance of a new day object
            if day.date.strftime("%A") == "Sunday" and distance < 7:
                week.append(day)
                break
            else:
                week.append(day)
                distance += 1
        weekstr = "week" + str(self.week)
        self.timeline[weekstr] = week                                 # adds a list of days object to the timeline dict
        self.week += 1                                                # increments the self.week variables


    def get_remaining(self, week):
        norm_week = ["Monday", "Thuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        length_remaining = 7 - len(week)
        return norm_week[0:length_remaining]
            
