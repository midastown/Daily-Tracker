from datetime import date, timedelta

class Day:

    def __init__(self, time_distance):
        self.activities = None
        self.mood       = None
        self.percentage = None
        self.metrics    = {}
        self.date       = date.today() + timedelta(days = time_distance)

    def add_new_metric(metric_str, data_structure):
        """
        This method lets you add an additional custom metric at runtime.
        This method can even replace the variables initiated on top if this helps the design.
        """
        pass


