import matplotlib
import numpy as np
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
        self.dayPercent = [50, 40, 30, 70, 70, 80,...]
        self.moods = [1, 2, 4, 1, 2, 2, 5,...]
        self.dates = [date(2020, 4, 1), date(2020, 4, 2), date(2020, 4, 3),...]
        """
        week = 1
        day = 0
        weekLength = len(t.timeline["week"+str(week)])
        currentDay = t.timeline["week"+str(week)][day]
        
        while currentDay.date != date.today():       # O(number of days until today in timeline)
            if currentDay.activities:
                count = 0
                for activity in currentDay.activities:   # O(number of activities in each day)
                    if activity[1].get_value() == 1:
                        count += 1
                percent = round((count * 100)/len(currentDay.activities))
            else:
                percent = 0
            self.dayPercent.append(percent)

            self.moods.append(currentDay.mood.get_value())
            self.dates.append(currentDay.date)
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
        """
        Get function for the data collected
        """
        return (self.dayPercent, self.moods, self.dates)


    def create_canvas(self, frame):
        """
        Creates the graph seen in the Statistics Tab, designed to show the correlation 
        between the number of activities done and the overall mood that particular day.
        """

        dates = np.array(self.dates)
        # Use tkinter for matplotlib
        matplotlib.use('TkAgg')

        # fig is pretty much the graph, ax1 is for plotting week against dayPercent, by having ax1
        # and ax2, it means we can plot them both on the same graph and have two different
        # y axis. figsize is the size of the window
        # do we need to predetermine the size rn, can we do that when drawing the canvas inside the tab ?
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.set_title('Percent Per Day')

        # lbl1 is a plot on ax1, but by creating a variable out of it we can combine with ax2.
        # by doing this, we can have both legends in the same area
        # g- is green
        # b- is blue
        ax1.set_xlabel('Date')
        lbl1 = ax1.plot(dates, self.dayPercent, 'g-',label='Acvitivies Done %')
        lbl2 = ax2.plot(dates, self.moods,'b-',label='Average Mood')
        
        # first and second y-axis formatting
        ax1.set_ylabel('Activity Done Percent')
        ax1.set_ylim(ymin=0, ymax=100)
        ax2.set_ylabel('Mood')
        ax2.set_ylim(ymin=1, ymax=10)

        # This will format the x-axis by displaying enough date object so that 
        # they do not overlap
        if dates.any():

            ax1.set_xlim((np.datetime64(dates[0]), np.datetime64(dates[-1])))
            locator = matplotlib.dates.AutoDateLocator(minticks=3, maxticks=7)
            formatter = matplotlib.dates.ConciseDateFormatter(locator)
            ax1.xaxis.set_major_locator(locator)
            ax1.xaxis.set_major_formatter(formatter)


        # here we put ax1s and ax2s 'attributes' together
        lbl = lbl1 + lbl2
        # here we get all the labels from them
        labs = [l.get_label() for l in lbl]
        # we then display their legends together
        ax1.legend(lbl,labs,loc=0)

        # basically this just shows the graph
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=1)
        canvas._tkcanvas.pack(fill="both", expand=1)

        # quits when closed
        plt.close('all')





