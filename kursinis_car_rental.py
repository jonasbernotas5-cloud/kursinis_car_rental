from abc import ABC, abstractmethod
import json

class Vehicle(ABC):
    def __init__(self, license_plate, model, daily_rate):
        self.license_plate = license_plate
        self._model = model
        self.daily_rate = daily_rate
        self._is_available = True

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
    

class Customer:
    def __init__(self, name, customer_ID):
        self.name = name
        self.customer_ID = customer_ID
        self._rented_vehicles = []

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not value or value.strip() == "":
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def customer_ID(self):
        return self._customer_ID
        
    @customer_ID.setter
    def customer_ID(self, value):
        if not(len(value) == 4 and value[0] == "C" and value[1:].isdigit()):
            raise ValueError("the ID is incorrect")
        self._customer_ID = value

    def add_rented_vehicle(self, vehicle):
        if not vehicle._is_available:
            raise ValueError(f"Vehicle {vehicle.license_plate} is not available for rent.")
        self._rented_vehicles.append(vehicle)

    def return_rented_vehicle(self, license_plate):
        vehicle = next((v for v in self._rented_vehicles if v.license_plate == license_plate), None)
        if vehicle:
            self._rented_vehicles.remove(vehicle)
            vehicle._is_available = True
            return f"Vehicle {license_plate} returned successfully."
        else:
            return f"Vehicle with license plate {license_plate} not found in rented vehicles."


class RentalSystem:
    def __init__(self):
        self._fleet = []
        self._customers = []

    def add_vehicle(self, vehicle):
        self._fleet.append(vehicle)

    def add_customer(self, customer):
        self._customers.append(customer)

    def rent_vehicle(self, customer_ID, license_plate, days):
        
        customer = next((c for c in self._customers if c.customer_ID == customer_ID), None)
        if not customer:
            return f"Customer with ID {customer_ID} not found."

        vehicle = next((v for v in self._fleet if v.license_plate == license_plate), None)
        if not vehicle:
            return f"Vehicle with license plate {license_plate} not found."
    
        if not vehicle._is_available:
            return f"Vehicle {license_plate} is not available for rent."
        
        
        total_price = vehicle.get_total_price(days)
        customer.add_rented_vehicle(vehicle)
        vehicle._is_available = False
        return f"Vehicle {license_plate} rented to customer {customer_ID} for {days} days. Total price: ${total_price:.2f}"

    def save_data(self, filename = "data.json"):
        data = {
            "fleet": [],
            "customers": []
        }
        for v in self._fleet:
            v_data = {
                "type": type(v).__name__,
                "license_plate": v.license_plate,
                "model": v._model,
                "daily_rate": v.daily_rate,
                "is_available": v._is_available
            }
            if isinstance(v, Car):
                v_data["extra_attribute"] = v.seats
            elif isinstance(v, Motorcycle):
                v_data["extra_attribute"] = v.engine_capacity
            elif isinstance(v, Truck):
                v_data["extra_attribute"] = v.load_capacity

            data["fleet"].append(v_data)

        for c in self._customers:
            c_data = {
                "name": c.name,
                "customer_ID": c.customer_ID,
                "rented_vehicles": [v.license_plate for v in c._rented_vehicles]
            }
            data["customers"].append(c_data)

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

        return f"Data saved to {filename} successfully."
    
    def load_data(self, filename = "data.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            for v_data in data["fleet"]:
                vehicle = Factory.create_vehicle(v_data["type"], v_data["license_plate"], v_data["model"], v_data["daily_rate"], v_data["extra_attribute"])
                vehicle._is_available = v_data["is_available"]
                self.add_vehicle(vehicle)

            for c_data in data["customers"]:
                customer = Customer(c_data["name"], c_data["customer_ID"])
                for license_plate in c_data["rented_vehicles"]:
                    vehicle = next((v for v in self._fleet if v.license_plate == license_plate), None)
                    if vehicle:
                        customer._rented_vehicles.append(vehicle)
                        vehicle._is_available = False
                self.add_customer(customer)

            return f"Data loaded from {filename} successfully."

        except FileNotFoundError:
            return f"File {filename} not found."

class Factory:
    @staticmethod
    def create_vehicle(vehicle_type, license_plate, model, daily_rate, extra_attribute):
        if vehicle_type == "Car":
            return Car(license_plate, model, daily_rate, extra_attribute)
        elif vehicle_type == "Motorcycle":
            return Motorcycle(license_plate, model, daily_rate, extra_attribute)
        elif vehicle_type == "Truck":
            return Truck(license_plate, model, daily_rate, extra_attribute)
        else:
            raise ValueError("Invalid vehicle type.")
        
# Example usage

if __name__ == "__main__":
    system = RentalSystem()

    try:
        car1 = Factory.create_vehicle("Car", "LRS123", "Toyota Corolla", 30, 5)
        truck1 = Factory.create_vehicle("Truck", "TRK789", "Volvo FH16", 100, 20000)
        motorcycle1 = Factory.create_vehicle("Motorcycle", "MTR456", "Yamaha MT-07", 20, 689)
        car2 = Factory.create_vehicle("Car", "LRS124", "Honda Civic", 28, 5)  
        
        system.add_vehicle(car1)
        system.add_vehicle(truck1)
        system.add_vehicle(motorcycle1)
        system.add_vehicle(car2)


        customer1 = Customer("John Doe", "C001")
        customer2 = Customer("Jane Smith", "C002")
        customer3 = Customer("David Johnson", "C003")  # This will raise an error due to invalid ID format

        system.add_customer(customer1)
        system.add_customer(customer2)
        system.add_customer(customer3)

    except Exception as e:
        print(f"Error during object creation: {e}")

    rental_result = [system.rent_vehicle("C001", "LRS123", 3)]
    rental_result.append(system.rent_vehicle("C002", "TRK789", 5))
    rental_result.append(system.rent_vehicle("C003", "MTR456", 2))
    
    print(f"Rental status: {rental_result}")

    save_status = system.save_data("data.json")
    print(save_status)

    new_system = RentalSystem()
    
    load_status = new_system.load_data("data.json")
    print(load_status)

    if len(new_system._fleet) > 0:
        v = new_system._fleet[0]
    for v in new_system._fleet:
        if v._is_available == False:
            display_status = "Rented"
        else:
            display_status = "Available"

        print(f"Restored Vehicle: {v._model} ({v.license_plate}), Status: {display_status}")
    
    for c in new_system._customers:
        rented_plates = [v.license_plate for v in c._rented_vehicles]
        print(f"Restored Customer: {c.name}, Rented Vehicles: {rented_plates}")