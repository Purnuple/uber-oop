from driver import Driver
from rider import Rider
from ride import Ride


class Uber:
    def __init__(self):
        self.available_drivers = []
        
    def add_driver(self, driver):
        self.available_drivers.append(driver)
    

    def __str__(self):
        result = " "
        for i in self.available_drivers:
            result += str(i) + "\n"
            
        return result
         

 
d1 = Driver("Drake","Bajaj")
d2 = Driver("Beyonce", "Fiat")
d3 = Driver("Nelly", "Banana Orange bus")
r1 = Rider("Rihanna")
ride1 = Ride(d1, r1,8)
app = Uber()

app.add_driver(d1)
app.add_driver(d2)
app.add_driver(d3)
print(app)