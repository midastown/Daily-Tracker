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
        self.days = []
        self.t = Timeline()
        self.t.add_week()
        
        for i in self.t.timeline["week"+str(self.week)]:
            self.days.append(i.date.strftime("%A"))
        print(self.days)
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
        # Frame creation
        frame1 = Frame(window)
        frame1.pack(fill="both")
        tablayout = Notebook(frame1)
        
        # Example of a tab that does nothing much but display text
        tab = Frame(tablayout)        # creating a nested frame
        tab.pack(fill="both")
        label = Label(tab, text="One can imagine adding cool stats about the tracking so far")
        label.pack() 
        tablayout.add(tab, text="Statistics")   # once its packed you can add it to the window object under a title

        # This is the Table layout in a new tab, so same logic as the one above but with more functionality
        tab = Frame(tablayout)
        tab.pack(fill="both")

        self.show_table(self.week, tab)

        he = Button(tab,text='hello',command=self.add_week)
        he.grid(row=10,column=0)
        # Oh crap there is no pack in this for loop at all, yeah man never
        # never, ever mix grid and pack, they are two seperate things.

        tablayout.add(tab, text="Current Week")  # once its grided this add it to the new tab under a different title 
       
       
        tablayout.pack(fill="both") # once everything is done now you pack the tablayout


    def show_table(self, week, tab, remaining=None):
        """
        This is the same mechanics that was working in create panel, now refactored in its own function
        
        """
        if len(self.days) < 7:
            hybrid_week = self.t.get_remaining(self.days) + self.days

        for i in range(len(self.activities)+1):              # for rows in activities
            for j in range(len(hybrid_week)+1):          # for cols in days
                if i == 0 and j == 0:                                  # if its first cell, add empty cell
                    label = Label(tab, text=" ")
                    label.grid(row=i, column=j)                        # this specifies where in the grid
                    tab.grid_columnconfigure(j, weight=1)              
                    # this last line makes the width of the column responsive to change in width of the window
                elif i == 0:           # adding the name of the day
                    label = Label(tab, text=hybrid_week[j-1])
                    label.grid(row=i, column=j)
                    tab.grid_columnconfigure(j, weight=1)
                elif j == 0:           # adding the name of the activity
                    label = Label(tab, text=self.activities[i-1])
                    label.grid(row=i, column=j)
                    tab.grid_columnconfigure(j, weight=1)
                else:                  # adding the checkboxes
                    if hybrid_week[j-1] in self.days:
                        label = Checkbutton(tab) 
                        label.grid(row=i, column=j)
                        tab.grid_columnconfigure(j, weight=1)
                    else:
                        label = Checkbutton(tab, state=DISABLED) 
                        label.grid(row=i, column=j)
                        tab.grid_columnconfigure(j, weight=1)


        
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




Panel(window, height, width).create_panel()

window.mainloop()
