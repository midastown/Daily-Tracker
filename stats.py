import matplotlib
from numpy import arange, sin, pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import date


class Stats():
    def __init__(self):
        self.dayPercent = []
        self.moods = []
        self.dates = []

    def set_variables(self, t):
        """
        Will loop through the timeline object and append computed data
        to its own dataList UNTIL IT REACH TODAY:
        self.dayPercent = [50, 40, 30, 70, 70, 80, ...]
        self.moods = [1, 2, 4, 1, 2, 2, 5, ...]
        self.dates = [(2020, 4, 1), (2020, 4, 2), (2020, 4, 3), (2020, 4, 4), ...]
        """
        week = 1
        day = 0
        weekLength = len(t.timeline["week"+str(week)])
        currentDay = t.timeline["week"+str(week)][day]
        
        last_day = t.timeline["week"+str(t.week - 1)][-1].date

        """
        while currentDay.date != date.today():       # O(number of days until today in timeline)
        """
        while currentDay.date != last_day:
            count = 0
            for activity in currentDay.activities:   # O(number of activities in each day)
                if activity[1].get_value() == 1:
                    count += 1
            percent = round((count * 100)/len(currentDay.activities))
            self.dayPercent.append(percent)
            self.moods.append(currentDay.mood.get_value())
            self.dates.append(currentDay.date.isoformat())
            if (day + 1) == weekLength:
                if ("week"+str(week + 1)) in t.timeline:
                    day = 0
                    week += 1
                    weekLength = len(t.timeline["week"+str(week)])
                    currentDay = t.timeline["week"+str(week)][day]
            else:
                day += 1
                currentDay = t.timeline["week"+str(week)][day]

    def get_variables(self):
        return (self.dayPercent, self.moods, self.dates)

    def create_canvas(self, frame):
         
        # Use tkinter for matplotlib
        matplotlib.use('TkAgg')

        # fig is pretty much the graph, ax1 is for plotting week against dayPercent, by having ax1
        # and ax2, it means we can plot them both on the same graph and have two different
        # y axis. figsize is the size of the window
        # do we need to predetermine the size rn, can we do that when drawing the canvas inside the tab ?
        fig, ax1 = plt.subplots(figsize=(9,4))
        ax2 = ax1.twinx()

        # lbl1 is a plot on ax1, but by creating a variable out of it we can combine with ax2.
        # by doing this, we can have both legends in the same area
        # g- is green
        # b- is blue
        lbl1 = ax1.plot(self.dates, self.dayPercent, 'g-',label='Acvitivies Done %')
        ax1.set_title('Percent Per Day')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Activity Done Percent')
        lbl2 = ax2.plot(self.dates, self.moods,'b-',label='Average Mood')
        ax2.set_ylabel('Mood')

        # here we put ax1s and ax2s 'attributes' together
        lbl = lbl1 + lbl2
        # here we get all the labels from them
        labs = [l.get_label() for l in lbl]
        # we then display their legends together
        ax1.legend(lbl,labs,loc=0)

        # basically this just shows the graph
        canvas = FigureCanvasTkAgg(fig, master=frame)
        """This will be done in create_panel"""
        #   canvas.draw()
        #   canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #   canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        # quits when closed
        plt.close('all')

        return canvas



