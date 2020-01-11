from tkinter import *
from tkinter.ttk import *

'''class Panel:

	def __init__(self):
		self.tree = ttk.Treeview(master)

	def create_panel(self):
		pan = Treeview(self)
    	pan['columns'] = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

	def add_activity(self):
		pass

	def remove_activity(self):
		pass

	def modify_mood(self):
		pass

	def modify_percent_done(self):
		pass'''

window = Tk()

tree = Treeview(window,height='15',columns=('emails','passwords'))
tree.heading("#0", text='Sources', anchor='w')
tree.column("#0", anchor="w")

treeview = tree

window.mainloop()



''' init -> table, activity_list,

toggle_checks -> add 1 for checked and 0 for unchecked

add_activity(activity_name) -> add a row in the activity section of the table, with checkboxes
remove_activity(activity_name) -> del a row in the activity section of the table.

modify_mood -> most likely from a selection of predefined moods

modify_percent_done -> from 0 to 100, making sure the user does not write down more or less. '''