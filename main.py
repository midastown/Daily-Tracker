from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font

height = 500
width = 1500

class Panel:

        def __init__(self,w,height,width):
                self.w = w
                self.height = height
                self.width = width
                self.activities = ['Activity 1', 'Activity 2', 'Activity 3', 'Activity 4', 'Activity 5']
                self.days = ['','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
                self.style = ttk.Style()
                self.style.configure("Treeview.Heading", font=(None, 15))
                self.style.configure('Treeview',rowheight=75)
                self.style.configure('Treeview',font=(None,20))
                self.style.configure('Treeview.Columns',rowheight=50)

        def create_panel(self):
        	self.tree = ttk.Treeview(self.w,height=self.height)
        	self.tree.pack()
        	self.tree['columns'] = (1,2,3,4,5,6,7)

        	for i in range(len(self.days)):
        		self.tree.heading("#"+str(i),text=self.days[i], anchor='w')

        	for i in range(len(self.activities)-1,-1,-1):
        		self.tree.insert('','0','item'+str(i),text=self.activities[i])
        		#self.tree.insert('','0','gap'+str(i),text='\n')
      

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