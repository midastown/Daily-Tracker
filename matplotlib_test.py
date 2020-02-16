import matplotlib
from numpy import arange, sin, pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import random
import timeline

def percent(a):		# This just returns a list of percent done for each day of week
	c = 0
	p = []

	for i in a:
		for k in i:
			if k == 1:
				c +=1
		p.append(int((c/len(a[0]))*100))
		print(c,len(a))
		c = 0

	return p

# Dummy data just for testing
posMoods = [1,2,3,4,5]

# Use tkinter for matplotlib
matplotlib.use('TkAgg')

window = Tk()
window.wm_title('Graph')

t = timeline.Timeline()
t.add_week()
t.add_week()

# Create random list of activities (done or not, 1 or 0, 5 for each day in week) for y axis
activities = [[random.randint(0,1) for i in range(5)] for k in range(len(t.timeline['week2']))]
# Gives list of dates in the week for x aixs
week = [t.timeline['week2'][i].date for i in range(len(t.timeline['week2']))]
# Choses random mood from posMoods, 1 being worst and 5 being best
moods = [random.choice(posMoods) for i in range(7)]

# acP just means activity percentage, is in list form, % for each day
acP = percent(activities)

# fig is pretty much the graph, ax1 is for plotting week against acP, by having ax1
# and ax2, it means we can plot them both on the same graph and have two different
# y axis. figsize is the size of the window
fig, ax1 = plt.subplots(figsize=(9,4))
ax2 = ax1.twinx()

# lbl1 is a plot on ax1, but by creating a variable out of it we can combine with ax2.
# by doing this, we can have both legends in the same area
# g- is green
lbl1 = ax1.plot(week,acP, 'g-',label='Acvitivies Done %')
ax1.set_title('Percent Per Day')
ax1.set_xlabel('Date')
ax1.set_ylabel('Activity Done Percent')

# b- is blue
lbl2 = ax2.plot(week,moods,'b-',label='Average Mood')
ax2.set_ylabel('Mood')

# here we put ax1s and ax2s 'attributes' together
lbl = lbl1 + lbl2
# here we get all the labels from them
labs = [l.get_label() for l in lbl]
# we then display their legends together
ax1.legend(lbl,labs,loc=0)

# basically this just shows the graph
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

# quits when closed
plt.close('all')

window.mainloop()

