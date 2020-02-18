from day import *
from datetime import date

class Timeline:

    def __init__(self):
        self.timeline = {}
        self.week = 1
        

    def add_week(self, distance=None):
        """
        Creates a new instance of a week and store it into the timeline
        Returns nothing.
        """
        week = []
        if not distance:
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


    def get_remaining(self, week_length):
        norm_week = ["Monday", "Thuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        length_remaining = 7 - week_length
        return norm_week[0:length_remaining]
            
    def add_activity(self, week, activity):
        """
        instantiate an activity in each day, or appends to an already instantiated variable
        """
        for i in self.t.timeline[week]:
            if i.activities:
                i.activities.append([activity, 0])
            else:                                       # activities = [[activity1, 0], [activity2, 0],...]
                                                        # activities = [[activity1, IntVar()], [activity2, IntVar()], ...]
                i.activities = [[activity, 0]]

    def get_activities_names(self, week):

        activities = week[0].activities
        if activities:                                        # if activities != None
            activity_names = []
            for i in activities:
                activity_name.append(i[0])
            return activity_names
        else:
            return [" "]














