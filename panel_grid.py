from tkinter import *
from tkinter.ttk import Notebook
from timeline import *
from main import *

class Panel:

    def __init__(self, window, heigth, width, t):
        self.window = window
        self.heigth = heigth
        self.width  = width
        self.week = 1
        self.t = t
        self.e = {}          # stores IntVars
        self.n = 0
        self.s = {}
        self.n2 = 0
        self.m = {}
        self.n3 = 0

    def create_panel(self):
        """
        this function shows two things, the tracker and a graph that shows the data tracked so far
        """
        # Main Frame creation
        frame1 = Frame(self.window)
        frame1.pack(fill="both")
        tablayout = Notebook(frame1)
 
        ##### TRACKER #####
        tab = Frame(tablayout)
        tab.pack(fill="both")
        table = Frame(tab)
        table.pack(fill="both")
        self.show_table(self.t.timeline["week" + str(self.week)], table)
        week_modifs = Frame(tab)
        week_modifs.pack(side=BOTTOM)
        next_week = Button(week_modifs,text='Next Week',command= lambda: self.next_week(table))
        next_week.pack(side=RIGHT)
        activityEntry = Entry(week_modifs)         
        activityEntry.pack(side=LEFT)
        b = Button(week_modifs,command=lambda: self.add_activity(activityEntry.get(), table),text='Add Activity')
        b.pack(side=LEFT)
        b = Button(week_modifs,command=lambda: self.remove_activity(activityEntry.get(),table),text='Remove Activity')
        b.pack(side=LEFT)
        last_week = Button(week_modifs,text='Last Week',command= lambda: self.last_week(table))
        last_week.pack(side=LEFT)
        save = Button(week_modifs, text="Save", command= lambda: self.save()) 
        save.pack(side=LEFT)
        tablayout.add(tab, text="Current Week")  # once its grided this add it to the new tab under a different title 
       
        
        ##### STATISTICS #####
        tab = Frame(tablayout)        # creating a nested frame
        tab.pack(fill="both")
        label = Label(tab, text="One can imagine adding cool stats about the tracking so far")
        label.pack() 
        tablayout.add(tab, text="Statistics")   # once its packed you can add it to the window object under a title
        tablayout.pack(fill="both") # once everything is done now you pack the tablayout
        

    def save(self):
        data = self.t
        pickle.dump(data, open('timeline-data/timeline.data', 'wb'), 4)

    def show_table(self, week, tab):
        """
        Creates a Table/Grid showing days, activities, checkboxes, ...
        """
        days = self.t.get_days_names(week)
        activities = self.t.get_activities_names(week)
        self.e = {}
        self.n = 0
        self.s = {}
        self.n2 = 0
        
        mood = [1,2,3,4,5,6,7,8,9,10]

        for i in range(len(activities)+2):              # for rows in activities
            for j in range(len(days)+1):                # for cols in days
                if i == 0 and j == 0:                                  # if its first cell, add empty cell
                    self.labeling(tab, i, j, Label(tab, text=" "))
                elif i == 0:                                           # adding the name of the day
                    self.labeling(tab, i, j, Label(tab, text=days[j-1]))
                elif i == (len(activities) + 1) and j == 0:
                    self.labeling(tab, i, j, Label(tab, text="mood"))
                elif i == (len(activities) + 1):
                    m = week[j-1].mood
                    self.s["e"+str(self.n2)] = StringVar(value=week[j-1].mood.get_value())
                    elem = OptionMenu(tab, self.s["e"+str(self.n2)], *mood, command=lambda mood=m, k=j-1: self.storeM(mood,k))
                    self.labeling(tab, i, j, elem)
                    self.n2 += 1
                elif activities[0] == " ":                             # if there are no activities 
                    self.labeling(tab, i, j, Label(tab, text=" "))
                elif j == 0:                                           # adding the name of the activity
                    self.labeling(tab, i, j, Label(tab, text=str(i) + ' - ' + activities[i-1]))
                elif i != (len(activities) + 1):                                                  # adding the checkboxes
                    c = week[j-1].activities[i-1][1]
                    self.e["e"+str(self.n)] = IntVar(value=c.get_value())
                    element = Checkbutton(tab, variable=self.e["e"+str(self.n)], command=lambda check=c : check.toggle())
                    self.labeling(tab, i, j, element)
                    self.n += 1

    def storeM(self, m, k):
        self.t.timeline["week"+str(self.week)][k].mood.set_value(m)


    def labeling(self, tab, i, j, element):
        """
        Does the labeling for show_table
        """
        label = element
        label.grid(row=i, column=j)                        # this specifies where in the grid
        tab.grid_columnconfigure(j, weight=1)              
        # this last line makes the width of the column responsive to change in width of the window
        

    def add_activity(self, activity, table):
        week = self.t.timeline["week" + str(self.week)]
        self.t.add_activity(week, activity)
        self.clear_frame(table)
        self.show_table(self.t.timeline["week" + str(self.week)], table)


    def remove_activity(self, activity, table):
        week = self.t.timeline['week' + str(self.week)]
        activityNum = int(activity) - 1
        self.t.remove_activity(week,activityNum)
        self.clear_frame(table)
        self.show_table(self.t.timeline['week' + str(self.week)], table)

    
    def next_week(self, table):
        """
        Does a few checks before showing the next week
        """
        if ("week" + str(self.week + 1)) not in self.t.timeline:
            self.t.add_week()
        self.week += 1
        self.clear_frame(table)
        self.show_table(self.t.timeline["week" + str(self.week)], table)


    def last_week(self, table):
        """
        Shows the last week if it exists
        """
        if self.week == 1:
            return
        self.week -= 1
        self.clear_frame(table)
        self.show_table(self.t.timeline["week" + str(self.week)], table)

    def clear_frame(self, table):
        for widget in table.winfo_children():
            widget.destroy()

