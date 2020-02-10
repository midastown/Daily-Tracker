from tkinter import *
from tkinter.ttk import Notebook
from timeline import *

width  = 800
height = 500

window = Tk()
window.title("Daily Tracker")
window.geometry(str(width) + "x" + str(height))

class Panel:

    def __init__(self, window, heigth, width):
        self.window = window
        self.heigth = heigth
        self.width  = width
        self.week = 1
        self.activities = ['Activity 1', 'Activity 2', 'Activity 3', 'Activity 4', 'Activity 5']
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.t = Timeline()
        self.t.add_week()
        
        # The way I do the grid, the fonts "need??" to be initiated when adding to the cells. Not sure about the
        # "need" but this is the way I found working, so maybe you can do better.


    def create_panel(self):
        """
        This function does a few things, first it creates frames, so that each frame is like a region in the 
        800 by 500 App. This helps with the organisation of content, in this case there is only one frame with tabs
        as its primary layout. But if for example you need to add buttons, you just create a new frame and you're not
        bound by the tab layout or the table layout

        I created the tab using the Notebook api from ttk. You can read about it in 
            https://wiki.tcl-lang.org/page/tkinter.Notebook
        """
        # Main Frame creation
        frame1 = Frame(window)
        frame1.pack(fill="both")
        tablayout = Notebook(frame1)
 
        # This is the tab with the Table 
        tab = Frame(tablayout)
        tab.pack(fill="both")

        table = Frame(tab)
        table.pack(fill="both")

        self.show_table(self.t.timeline["week" + str(self.week)], table)

        week_modifs = Frame(tab)
        week_modifs.pack(side=BOTTOM)
        next_week = Button(week_modifs,text='next',command= lambda: self.next_week(table))
        next_week.pack(side=RIGHT)
        last_week = Button(week_modifs,text='last',command= lambda: self.last_week(table))
        last_week.pack(side=LEFT)
    


        tablayout.add(tab, text="Current Week")  # once its grided this add it to the new tab under a different title 
       
        
        # Example of a tab that does nothing much but display text
        tab = Frame(tablayout)        # creating a nested frame
        tab.pack(fill="both")
        label = Label(tab, text="One can imagine adding cool stats about the tracking so far")
        label.pack() 
        tablayout.add(tab, text="Statistics")   # once its packed you can add it to the window object under a title
      
        tablayout.pack(fill="both") # once everything is done now you pack the tablayout


    def show_table(self, week, tab):
        """
        Creates a Table/Grid showing days, activities, checkboxes, ...
        """
        if len(week) < 7:
            current_week = [i.date.strftime("%A") for i in week]
            hybrid_week = self.t.get_remaining(len(week)) + current_week
        else:
            hybrid_week = []

        for i in range(len(self.activities)+1):              # for rows in activities
            for j in range(len(self.days)+1):                # for cols in days
                if i == 0 and j == 0:                                  # if its first cell, add empty cell
                    self.labeling(tab, i, j, Label(tab, text=" "))
                elif i == 0:                                           # adding the name of the day
                    self.labeling(tab, i, j, Label(tab, text=self.days[j-1]))
                elif j == 0:                                           # adding the name of the activity
                    self.labeling(tab, i, j, Label(tab, text=self.activities[i-1]))
                else:                                                  # adding the checkboxes
                    if hybrid_week:
                        if hybrid_week[j-1] in current_week:
                            self.labeling(tab, i, j, Checkbutton(tab))
                        else:
                            self.labeling(tab, i, j, Checkbutton(tab, state=DISABLED))
                    else:
                        self.labeling(tab, i, j, Checkbutton(tab))


    def labeling(self, tab, i, j, element):
        """
        Does the labeling for show_table
        """
        label = element
        label.grid(row=i, column=j)                        # this specifies where in the grid
        tab.grid_columnconfigure(j, weight=1)              
        # this last line makes the width of the column responsive to change in width of the window
        

    def add_week(self):
        pass

    def add_activity(self):
        pass

    def remove_activity(self):
        pass

    def modify_mood(self):
        pass

    def modify_percent_done(self):
        pass
    
    def next_week(self, table):
        """
        Does a few checks before showing the next week
        """
        if ("week" + str(self.week + 1)) not in self.t.timeline:
            self.t.add_week()
        
        self.week += 1
        self.show_table(self.t.timeline["week" + str(self.week)], table)


    def last_week(self, table):
        """
        Shows the last week if it exists
        """
        if self.week == 1:
            return

        self.week -= 1
        self.show_table(self.t.timeline["week" + str(self.week)], table)



Panel(window, height, width).create_panel()

window.mainloop()
