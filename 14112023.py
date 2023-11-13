# COPY Method
cars =["Saab", "Volvo", "BMW"]
new_cars = list(cars)
more_cars=["Honda"]
# new_cars = list(cars)
new_cars = cars.copy()
print(new_cars)

# EXTEND Method
cars.extend(more_cars)  # more_carsの内容をcarsに追加します。(Add the contents of more_cars to CARS.)
print(cars)

# JOIN Method
even_more_cars = new_cars + more_cars
print(even_more_cars)

# String Slicing
print(cars[1:2])
newCars = cars[1:2]
print(newCars)

cars =["Saab", "Volvo", "BMW"]
print(cars[-3:-1])
print(cars[1:-1])