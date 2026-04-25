from abc import ABC, abstractmethod

class Vehicle(ABC):
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


class Motorcycle(Vehicle):
    def __init__(self, license_plate, model, daily_rate, engine_capacity):
        super().__init__(license_plate, model, daily_rate)
        self._engine_capacity = engine_capacity

    def get_total_price(self, days):
        return ((self._daily_rate * days) * 0.5 + (self._engine_capacity * 0.1))

    def get_info(self):
        return f"{super().get_info()}, Engine Capacity: {self._engine_capacity}"
    

class Truck(Vehicle):
    def __init__(self, license_plate, model, daily_rate, load_capacity):
        super().__init__(license_plate, model, daily_rate)
        self._load_capacity = load_capacity

    def get_total_price(self, days):
        return (self._daily_rate * days) + (self._load_capacity * 0.2)

    def get_info(self):
        return f"{super().get_info()}, Load Capacity: {self._load_capacity}"
    

