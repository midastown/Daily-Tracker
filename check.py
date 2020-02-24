class Check():
    def __init__(self):
        self.value = 0

    def toggle(self):
        self.value ^= 1

    def get_value(self):
        return self.value