import pickle
from panel_grid import * 


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
    pickle.dump(t, open('timeline-data/timeline.data', 'wb'), 4)


def loadTimeline(found):
    """
    This will load a timeline object from timeline.data if it is found,
    otherwise it will create a new timeline object.
    Returns: a Timeline Object
    """
    if found:
        t = pickle.load(open('timeline-data/timeline.data', 'rb')) 
        print(t.timeline)
    else:
        t = Timeline()

    return t



if __name__ == "__main__":

    width, height = (800, 500)
    window = Tk()
    window.title("Daily Tracker")
    window.geometry(str(width) + "x" + str(height))
    
    try:
        f = open("timeline-data/timeline.data")
        f.close()
        found = True
    except FileNotFoundError:
        found = False

    t = loadTimeline(found)
    cleanUpTimeline(t)
    saveTimeline(t)
    Panel(window, height, width, t).create_panel()

    window.mainloop()

