# Author: Gautam Mehla
# File Name: car_details.py
# Description: This program collects information about a car, stores it in an Automobile object,
# and then displays the details in a user-friendly format. The program includes a Vehicle superclass
# and an Automobile subclass to model different types of vehicles.


class Vehicle:

  def __init__(self, vehicle_type):
    self.vehicle_type = vehicle_type


class Automobile(Vehicle):

  def __init__(self, vehicle_type, year, make, model, doors, roof):
    super().__init__(vehicle_type)
    self.year = year
    self.make = make
    self.model = model
    self.doors = doors
    self.roof = roof

  def display_info(self):
    print("Vehicle type:", self.vehicle_type)
    print("Year:", self.year)
    print("Make:", self.make)
    print("Model:", self.model)
    print("Number of doors:", self.doors)
    print("Type of roof:", self.roof)


def main():
  # Get user input
  vehicle_type = input(
      "Enter the vehicle type (e.g., car, truck, plane, boat, broomstick): ")
  year = input("Enter the year: ")
  make = input("Enter the make: ")
  model = input("Enter the model: ")
  doors = input("Enter the number of doors (2 or 4): ")
  roof = input("Enter the type of roof (solid or sun roof): ")

  # Create an instance of the Automobile class
  car = Automobile(vehicle_type, year, make, model, doors, roof)

  # Display the information
  car.display_info()


if __name__ == "__main__":
  main()
