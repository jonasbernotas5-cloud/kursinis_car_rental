import unittest
import os
import json
from kursinis_car_rental import Car, Truck, Customer, RentalSystem, Factory

class TestCarRentalSystem(unittest.TestCase):
    def setUp(self):
        self.system = RentalSystem()
        self.car = Factory.create_vehicle("Car", "LRS123", "Toyota Camry", 50, 5)
        self.motorcycle = Factory.create_vehicle("Motorcycle", "MTR456", "Honda CBR", 30, 600)
        self.truck = Factory.create_vehicle("Truck", "TRK789", "Ford F-150", 80, 1000)
        self.customer = Customer("John Doe", "C001")
        self.system.add_vehicle(self.car)
        self.system.add_vehicle(self.motorcycle)
        self.system.add_vehicle(self.truck)
        self.system.add_customer(self.customer)

    def test_create_car(self):
        
        car = Factory.create_vehicle("Car", "LRS123", "Toyota Camry", 50, 5)
        self.assertIsInstance(car, Car)
        self.assertEqual(car.license_plate, "LRS123")
        self.assertEqual(car._model, "Toyota Camry") 
        self.assertEqual(car.daily_rate, 50)
        self.assertEqual(car.seats, 5)
    
    def test_create_customer(self):
        customer = Customer("John Doe", "C001")
        self.assertIsInstance(customer, Customer)
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.customer_ID, "C001") 

    def test_license_plate_validation(self):
        with self.assertRaises(ValueError):
            self.car.license_plate = "123ABC"
        with self.assertRaises(ValueError):
            self.car.license_plate = "LRS12"
    
    def test_vehicle_daily_rate_validation(self):
        with self.assertRaises(ValueError):
            self.car.daily_rate = -5

    def test_customer_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("", "C002")

    def test_customer_id_validation(self):
        with self.assertRaises(ValueError):
            self.customer.customer_ID = "A001"
        with self.assertRaises(ValueError):
            self.customer.customer_ID = "C12"
        with self.assertRaises(ValueError):
            self.customer.customer_ID = "C00J"

    def test_car_seats_validation(self):
        with self.assertRaises(ValueError):
            self.car.seats = 0
        with self.assertRaises(ValueError):
            self.car.seats = -3

    def test_motorcycle_seats_validation(self):
       with self.assertRaises(ValueError):
            self.motorcycle.engine_capacity = 0

    def test_truck_load_capacity_validation(self):
        with self.assertRaises(ValueError):
            self.truck.load_capacity = 0
        with self.assertRaises(ValueError):
            self.truck.load_capacity = -5

    def test_car_price_calculation(self):
        self.assertEqual(self.car.get_total_price(2), 125)

    def test_motorcycle_price_calculation(self):
        self.assertEqual(self.motorcycle.get_total_price(3), 150)

    def test_truck_price_calculation(self):
        self.assertEqual(self.truck.get_total_price(1), 280)

    def test_successful_rent(self):
        result = self.system.rent_vehicle("C001", "LRS123", 2)
        self.assertIn("rented to customer", result)
        self.assertFalse(self.car._is_available)
        self.assertEqual(len(self.customer._rented_vehicles), 1)

    def test_rent_already_rented_vehicle(self):
        self.system.rent_vehicle("C001", "LRS123", 1)
        result = self.system.rent_vehicle("C001", "LRS123", 1)
        self.assertEqual(result, "Vehicle LRS123 is not available for rent.")

    def test_multiple_rentals_to_one_customer(self):
        """Tikrina, ar tas pats klientas gali išsinuomoti kelias priemones."""
        self.system.rent_vehicle("C001", "LRS123", 1) 
        self.system.rent_vehicle("C001", "TRK789", 1) 
        self.assertEqual(len(self.customer._rented_vehicles), 2)
        self.assertFalse(self.car._is_available)
        self.assertFalse(self.truck._is_available)

    def test_return_vehicle_logic(self):
        self.system.rent_vehicle("C001", "LRS123", 1)
        self.customer.return_rented_vehicle("LRS123")
        self.assertTrue(self.car._is_available)
        self.assertEqual(len(self.customer._rented_vehicles), 0)

    def test_rent_non_existent_vehicle(self):
        result = self.system.rent_vehicle("C001", "XYZ000", 1)
        self.assertEqual(result, "Vehicle with license plate XYZ000 not found.")

    def test_rent_non_existent_customer(self):
        result = self.system.rent_vehicle("C999", "LRS123", 1)
        self.assertEqual(result, "Customer with ID C999 not found.")

    def test_json_save_and_load_state(self):
        self.system.rent_vehicle("C001", "LRS123", 5)
        self.system.save_data("unittest_data.json")
        
        new_system = RentalSystem()
        new_system.load_data("unittest_data.json")
        
        restored_car = next(v for v in new_system._fleet if v.license_plate == "LRS123")
        self.assertFalse(restored_car._is_available)
        
        if os.path.exists("unittest_data.json"):
            os.remove("unittest_data.json")

    def test_factory_invalid_type(self):
        with self.assertRaises(ValueError):
            Factory.create_vehicle("Plane", "PLN123", "Boeing", 500, 200)

    def test_factory_creates_correct_instance(self):
        truck = Factory.create_vehicle("Truck", "TRK001", "Scania", 150, 5000)
        self.assertIsInstance(truck, Truck)

if __name__ == '__main__':
    unittest.main()