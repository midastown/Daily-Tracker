import matplotlib
from numpy import arange, sin, pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import random
import timeline

def percent(a):
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

posMoods = [1,2,3,4,5]

matplotlib.use('TkAgg')

window = Tk()
window.wm_title('Graph')

t = timeline.Timeline()
t.add_week()
t.add_week()

activities = [[random.randint(0,1) for i in range(5)] for k in range(7)]
week = [t.timeline['week2'][i].date for i in range(len(t.timeline['week2']))]
moods = [random.choice(posMoods) for i in range(7)]

#f = Figure(figsize=(8,4),dpi=(100))
#a = f.add_subplot(111)
days = week
acP = percent(activities)

fig, ax1 = plt.subplots(figsize=(9,4))
ax2 = ax1.twinx()

# x y
lns1 = ax1.plot(days,acP, 'g-',label='Acvitivies Done %')
ax1.set_title('Percent Per Day')
ax1.set_xlabel('Date')
ax1.set_ylabel('Activity Done Percent')

lns2 = ax2.plot(days,moods,'b-',label='Average Mood')
ax2.set_ylabel('Mood')

lns = lns1 + lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns,labs,loc=0)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

plt.close('all')

window.mainloop()

