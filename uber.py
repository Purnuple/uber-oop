from driver import Driver
from rider import Rider
from ride import Ride
import random


class Uber:
    def __init__(self):
        self.available_drivers = []
        self.active_rides = []
        self.completed_rides = []
        

    def add_driver(self, driver):
        self.available_drivers.append(driver)
    

    def request_ride(self, rider, distance):
        random_driver = self.available_drivers.pop()
        ride1 = Ride(random_driver,rider, distance)
        self.active_rides.append(ride1)
        random_driver.available = False
        return ride1

    def mark_ride_completed(self, ride):
        ride.driver.available = True
        self.completed_rides.append(ride)
        self.active_rides.remove(ride)
        return ride
    
      
    def __str__(self):
        result = ""
        for i in self.available_drivers:
            result += str(i) + "\n"
        for k in self.active_rides:
            result+= str(k) + "\n"
        for j in self.completed_rides:
            result += str(j) + "\n"
        return result

        

         

 
# d1 = Driver("Drake","Bajaj")
# d2 = Driver("Beyonce", "Fiat")
# d3 = Driver("Nelly", "Bus")
# r1 = Rider("Father Elvis")
# r2 = Rider("Gerald")

# # ride1 = Ride("Pharsa", "Hanabi", 8 )
# # ride2 = Ride("No", "jay", 9)
# app = Uber()
# app.add_driver(d1)
# app.add_driver(d2)
# app.add_driver(d3)



# ride1 = app.request_ride(r1,6)

# ride1.start_ride()


# ride1.complete_ride()

# app.mark_ride_completed(ride1)

# print(ride1.driver.available == True)

# print(ride1 in app.completed_rides)
# print(ride1 not in app.active_rides)


