from tkinter import Scale, Tk, Frame, Label, Checkbutton
from tkinter.ttk import Notebook

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
        self.activities = ['Activity 1', 'Activity 2', 'Activity 3', 'Activity 4', 'Activity 5']
        self.days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
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

        for i in range(6):              # for rows in activities
            for j in range(8):          # for cols in days
                if i == 0 and j == 0:                                  # if its first cell, add empty cell
                    label = Label(tab, text=" ")
                    label.grid(row=i, column=j)                        # this specifies where in the grid
                    tab.grid_columnconfigure(j, weight=1)              
                    # this last line makes the width of the column responsive to change in width of the window
                elif i == 0:           # adding the name of the day
                    label = Label(tab, text=self.days[j-1])
                    label.grid(row=i, column=j)
                    tab.grid_columnconfigure(j, weight=1)
                elif j == 0:           # adding the name of the activity
                    label = Label(tab, text=self.activities[i-1])
                    label.grid(row=i, column=j)
                    tab.grid_columnconfigure(j, weight=1)
                else:                  # adding the checkboxes
                    label = Checkbutton(tab) 
                    label.grid(row=i, column=j)
                    tab.grid_columnconfigure(j, weight=1)
        
        # Oh shit there is no pack in this for loop at all, yeah man never
        # never, ever mix grid and pack, they are two seperate things.

        tablayout.add(tab, text="Current Week")  # once its grided this add it to the new tab under a different title 
       
       
        tablayout.pack(fill="both") # once everything is done now you pack the tablayout


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


