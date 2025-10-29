class Rider:
    def __init__(self, name):
        self.name = name
        self.ride_history = []

    def __str__(self):
        return f"{self.name}"

rider1 = Rider("Nothando")
