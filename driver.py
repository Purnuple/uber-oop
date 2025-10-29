class Driver:
    def __init__(self, name, car_model):
        self.name = name
        self.car_model = car_model
        self.available = True
        self.completed_rides = []

    def __str__(self):
        return f"{self.name}, {self.car_model}, {self.available},{self.completed_rides}"

driver1 = Driver("Nothando", "Ford")
print(driver1)