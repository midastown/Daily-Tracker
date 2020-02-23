from tkinter import *
from tkinter.ttk import Notebook
from timeline import *
from main import *
#   width  = 800
#   height = 500

#   window = Tk()
#   window.title("Daily Tracker")
#   window.geometry(str(width) + "x" + str(height))

class Panel:

    def __init__(self, window, heigth, width, t):
        self.window = window
        self.heigth = heigth
        self.width  = width
        self.week = 1
        self.t = t

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
        frame1 = Frame(self.window)
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
       
        
        # Example of a tab that does nothing much but display text
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

        for i in range(len(activities)+1):              # for rows in activities
            for j in range(len(days)+1):                # for cols in days
                if i == 0 and j == 0:                                  # if its first cell, add empty cell
                    self.labeling(tab, i, j, Label(tab, text=" "))
                elif i == 0:                                           # adding the name of the day
                    #print( "This is j: " + str(j) + ", this is i: " + str(i))
                    self.labeling(tab, i, j, Label(tab, text=days[j-1]))
                elif activities[0] == " ":                             # if there are no activities 
                    self.labeling(tab, i, j, Label(tab, text=" "))
                elif j == 0:                                           # adding the name of the activity
                    self.labeling(tab, i, j, Label(tab, text=str(i) + ' - ' + activities[i-1]))
                else:                                                  # adding the checkboxes
                    # TODO: implement the check object instead of intvar
                    print(week[j-1].activities[i-1][1])

                    element = Checkbutton(tab, command= lambda: self.toggle(i, j))
                    if week[j-1].activities[i-1][1] == 1:
                        element.select()                 
                    self.labeling(tab, i, j, element)

    def toggle(self, i, j):
        if self.t.timeline["week" + str(self.week)][j-1].activities[i-1][1] == 1:
            self.t.timeline["week" + str(self.week)][j-1].activities[i-1][1] = 0
        else:
            self.t.timeline["week" + str(self.week)][j-1].activities[i-1][1] = 1

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

    def add_activity(self, activity, table):
        week = self.t.timeline["week" + str(self.week)]
        self.t.add_activity(week, activity)
        self.show_table(self.t.timeline["week" + str(self.week)], table)

    def remove_activity(self, activity, table):
        week = self.t.timeline['week' + str(self.week)]
        activityNum = int(activity) - 1
        self.t.remove_activity(week,activityNum)
        self.clear_frame(table)
        self.show_table(self.t.timeline['week' + str(self.week)], table)

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

#   Panel(window, height, width).create_panel()

#   window.mainloop()
