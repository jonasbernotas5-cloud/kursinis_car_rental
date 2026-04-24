from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, license_plate, model, daily_rate):
        self._license_plate = license_plate
        self._model = model
        self._daily_rate = daily_rate
    
    @abstractmethod
    def get_total_price(self, days):
        pass
    
    
    def get_info(self):
        return f"License Plate: {self._license_plate}, Model: {self._model}, Daily Rate: {self._daily_rate}"
    
    
    
class Car(Vehicle):
    def __init__(self, license_plate, model, daily_rate, seats):
        super().__init__(license_plate, model, daily_rate)
        self._seats = seats
    
    def get_total_price(self, days):
        return (self._daily_rate * days) + (self._seats * 5)
    
    def get_info(self):
        return f"{super().get_info()}, Seats: {self._seats}"
    


    