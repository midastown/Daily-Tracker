from day import *

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
        distance = 0
        for i in range(7):
            day = Day(distance)
            if day.strftime("%A") == "Sunday" and distance < 7:
                break
            else:
                week.append(day)
                distance += 1
        weekstr = "week" + str(self.week)
        self.timeline[weekstr] = week

            
