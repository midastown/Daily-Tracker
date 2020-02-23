

class Check():
    def __init__(self):
        self.value = 0

    def toggle(self):
        if self.value == 0:
            self.value = 1
        else:
            self.value = 0
