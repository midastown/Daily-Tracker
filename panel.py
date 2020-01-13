from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
from timeline import *


height = 500
width = 1625

class Panel:

        def __init__(self,w,height,width):
                self.week = 1
                self.t = Timeline()
                self.t.add_week()
                self.w = w
                self.height = height
                self.width = width
                self.activities = ['Activity 1', 'Activity 2', 'Activity 3', 'Activity 4', 'Activity 5','Activity 6']
                self.days = ['','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
                self.style = ttk.Style()
                self.style.configure("Treeview.Heading", font=(None, 17))
                self.style.configure('Treeview',rowheight=75)
                self.style.configure('Treeview',font=(None,20))
                self.style.configure('Treeview.Columns',rowheight=50)

        def create_panel(self):
        	self.tree = ttk.Treeview(self.w,height=self.height)
        	self.tree.pack()
                print(self.t.timeline)
        	self.tree['columns'] = [i for i in range(len(self.t.timeline['week'+str(self.week)]))]

                self.tree.heading('#0',text='')
        	for i in range(len(self.t.timeline['week1'])):
        		self.tree.heading("#"+str(i+1),text=self.t.timeline['week'+str(self.week)][i].date.strftime('%A'), anchor='w')

        	self.tree.insert('','0','percent done',text='Percentage Done') 
        	self.tree.insert('','0','overall mood',text='Overall Mood') 

        	for i in range(len(self.activities)-1,-1,-1):
        		self.tree.insert('','0','activity'+str(i),text=self.activities[i]) 
 

        def add_activity(self):
                pass

        def remove_activity(self):
                pass

        def modify_mood(self):
                pass

        def modify_percent_done(self):
                pass

window = Tk()
window.geometry(str(width)+'x'+str(height))

Panel(window,height,width).create_panel()

window.mainloop()

