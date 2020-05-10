from datetime import date, timedelta

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


    def get_days_names(self, week):
        days = []
        for i in week:
            days.append(i.date.strftime("%A"))
        return days

            
    def add_activity(self, week, activity):
        """
        instantiate an activity in each day, or appends to an already instantiated variable
        # activities = [[activity1, 0], [activity2, 0],...]
        # activities = [[activity1, Check()], [activity2, Check()], ...]
        """
        for i in week:
            c = Check()
            if i.activities:
                i.activities.append([activity, c])
            else:                           
                i.activities = [[activity, c]]

    def remove_activity(self, week, activityNum):
        for i in week:
            del i.activities[activityNum]

    def get_activities_names(self, week):

        activities = week[0].activities
        if activities:                                        # if activities != None
            activity_names = []
            for i in activities:
                activity_names.append(i[0])
            return activity_names
        else:
            return [" "]


class Day:
    def __init__(self, time_distance):
        self.activities = None
        self.mood       = Mood() 
        self.percentage = None
        self.metrics    = {}
        self.date       = date.today() + timedelta(days = time_distance)


class Mood():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class Check():
    def __init__(self):
        self.value = 0

    def toggle(self):
        self.value ^= 1

    def get_value(self):
        return self.value
