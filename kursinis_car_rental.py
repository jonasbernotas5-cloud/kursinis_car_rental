from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_plate, model, daily_rate):
        self.license_plate = license_plate
        self._model = model
        self.daily_rate = daily_rate

    @property
    def license_plate(self):
        return self._license_plate
    
    @license_plate.setter
    def license_plate(self, value):
        if not(len(value) == 6 and value[:3].isalpha() and value[3:].isdigit()):
            raise ValueError("license plate must be in format ABC123")
        self._license_plate = value

    @property
    def daily_rate(self):
        return self._daily_rate
    
    @daily_rate.setter
    def daily_rate(self, value):
        if value <= 0:
            raise ValueError("Daily rate cannot be zero or negative.")
        self._daily_rate = value

    @abstractmethod
    def get_total_price(self, days):
        pass
    
    def get_info(self):
        return f"License Plate: {self._license_plate}, Model: {self._model}, Daily Rate: {self._daily_rate}"
    
    
class Car(Vehicle):
    def __init__(self, license_plate, model, daily_rate, seats):
        super().__init__(license_plate, model, daily_rate)
        self.seats = seats

    @property
    def seats(self):
        return self._seats
    
    @seats.setter
    def seats(self, value):
        if value < 1:
            raise ValueError("Seats must be at least 1.")
        self._seats = value

    def get_total_price(self, days):
        return (self._daily_rate * days) + (self._seats * 5)

    def get_info(self):
        return f"{super().get_info()}, Seats: {self._seats}"


class Motorcycle(Vehicle):
    def __init__(self, license_plate, model, daily_rate, engine_capacity):
        super().__init__(license_plate, model, daily_rate)
        self.engine_capacity = engine_capacity

    @property
    def engine_capacity(self):
        return self._engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, value):
        if value < 50:
            raise ValueError("Engine capacity must be at least 50.")
        self._engine_capacity = value

    def get_total_price(self, days):
        return (self._daily_rate * days) + (self._engine_capacity * 0.1)

    def get_info(self):
        return f"{super().get_info()}, Engine Capacity: {self._engine_capacity}"
    

class Truck(Vehicle):
    def __init__(self, license_plate, model, daily_rate, load_capacity):
        super().__init__(license_plate, model, daily_rate)
        self.load_capacity = load_capacity

    @property
    def load_capacity(self):
        return self._load_capacity
    
    @load_capacity.setter
    def load_capacity(self, value):
        if value <= 0:
            raise ValueError("load capacity cannot be zero or negative")
        self._load_capacity = value

    def get_total_price(self, days):
        return (self._daily_rate * days) + (self._load_capacity * 0.2)

    def get_info(self):
        return f"{super().get_info()}, Load Capacity: {self._load_capacity}"
    