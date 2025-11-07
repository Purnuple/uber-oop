class Driver:
    def __init__(self, name, car_model):
        self.name = name
        self.car_model = car_model
        self.available = True
        self.completed_rides = []
        self.ratings = []

    @property
    def average_rating(self):
        length = len(self.ratings)
        sumofrates = sum(self.ratings)
        return sumofrates/length


    def __str__(self):
        return f"{self.name}, {self.car_model}, {self.available},{self.completed_rides}, {self.average_rating}"
