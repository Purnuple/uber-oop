import driver
import rider

class Ride:

    def __init__(self, driver, rider, distance):
        self.driver = driver
        self.rider = rider
        self.distance = distance
        self.status = "requested"
        self.RATE_PER_KM = 10
        self.cost = distance * self.RATE_PER_KM


    def start_ride(self):
        self.status = "in_progress"
        return self.status

    def complete_ride(self):
        self.status = "completed"
        return self.status

    def __str__(self):
        return f"{self.driver},{self.rider},{self.distance},{self.status}"




ride1 = Ride("Nothando","Fred",5)
ride1.start_ride()
print(ride1)
ride1.complete_ride()
print(ride1)



