class Rider:
    def __init__(self, name):
        self.name = name
        self.ride_history = []

    def rate_driver(self,driver, rate):
        driver.ratings.append(rate)
    
    def __str__(self):
        return f"{self.name}"

# rider1 = Rider("Nothando")
