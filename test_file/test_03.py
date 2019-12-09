# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title()+" is now sitting")
#
#     def roll_over(self):
#         print(self.name.title()+" rolled over")
#
#
# my_dog = Dog('popy','12')
# my_dog.sit()
# my_dog.roll_over()






#
# class Car():
#     def __init__(self,make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = '{} {} {}'.format(str(self.year),self.make, self.model)
#         return long_name.title()
#
#     def read_odometer(self):
#         print('This car has {} miles on it'.format(self.odometer_reading))
#
#     def update_odometer(self,mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer')
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

#
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print('The restaurant name is '+self.restaurant_name.title())
#         print('The cuisine type is ' + self.cuisine_type.title())
#
#     def open_restaurant(self):
#         print('The restaurant is open')
#
#     def served_restaurant(self,restaurant):
#         self.number_served = restaurant
#         print('{} people have eaten in a restaurant'.format(self.number_served))
#
#     def set_number_served(self,set_number):
#         self.set_number = set_number
#         print('Table for {}'.format(set_number))
#
#     def increment_number_served(self,increment_number):
#         self.set_number += increment_number
#         print('I think table for {}'.format(self.set_number))
#
#
# restaurant = Restaurant('BF', 'chinese food')
# restaurant.served_restaurant(5)
# print(restaurant.number_served)
# restaurant.set_number_served(100)
# restaurant.increment_number_served(10)

class User():
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("The User name is {}.{}".format(self.first_name,self.last_name))
        print('The user logged in {} times '.format(self.login_attempts))

    def greet_user(self):
        print('Hello, {}.{}'.format(self.first_name,self.last_name))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('allen','tommy')
user.describe_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.describe_user()
user.reset_login_attempts()
user.describe_user()


