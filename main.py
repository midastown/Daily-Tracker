import pickle
import os
from panel_grid import * 
from stats import Stats

def cleanUpTimeline(t):
    """
    this will clean up the timeline object by adding the right amount of 
    weeks missing from last date to today.
    """
    if t.week == 1:
        t.add_week()
    else:
        last_day = t.timeline["week" + str(t.week - 1)][-1].date
        distance = (last_day - date.today()).days + 1
        
        while distance < 0:
            t.add_week(distance)
            distance += 7

def saveTimeline(t):
    """
    This will save the timeline object in timeline.data.
    """
    with open('timeline-data/timeline.data', 'wb') as f:
        pickle.dump(t, f, 4)


def loadTimeline(found):
    """
    This will load a timeline object from timeline.data if it is found,
    otherwise it will create a new timeline object.
    Returns: a Timeline Object
    """
    if found:
        with open('timeline-data/timeline.data', 'rb') as f:
            t = pickle.load(f)
    else:
        t = Timeline()

    return t



if __name__ == "__main__":

    width, height = (800, 500)
    window = Tk()
    window.title("Daily Tracker")
    window.geometry(str(width) + "x" + str(height))

    found = os.path.isfile("timeline-data/timeline.data")

    t = loadTimeline(found)
    cleanUpTimeline(t)
    saveTimeline(t)
    s = Stats()
    s.set_variables(t)
    
    data = s.get_variables()
    for e in data:
        print(e)
    


    Panel(window, height, width, t, s).create_panel()

    window.mainloop()
