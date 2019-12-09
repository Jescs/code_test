class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = '{} {} {}'.format(str(self.year), self.make, self.model)
        return long_name.title()

    def read_odometer(self):
        print('This car has {} miles on it'.format(self.odometer_reading))

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print('This car\'s gas tank is full')


class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a {}-kwh battery'.format(self.battery_size))

    def get_range(self):
        if self.battery_size ==70:
            range = 240
        elif self.battery_size ==85:
            range = 270
        message = 'This car can go approximately {} miles on a full charge'.format(range)
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print('This car doesn\'t need a gas tank')


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


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
# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = [restaurant_name]
#
#     def show_icecream(self):
#         print("The icecream\'s name is {}, its cuisine type is {}".format(self.restaurant_name,self.cuisine_type))
#
#
# ice_cream = IceCreamStand('apple_icecream','apple')
# ice_cream.show_icecream()

# class User():
#     def __init__(self,first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print("The User name is {}.{}".format(self.first_name,self.last_name))
#         print('The user logged in {} times '.format(self.login_attempts))
#
#     def greet_user(self):
#         print('Hello, {}.{}'.format(self.first_name,self.last_name))
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# class Privileges():
#     def __init__(self):
#         self.privileges = ['can add post', 'can delete post', 'can ban user']
#
#     def show_privileges(self, i):
#         print('The user\'s permissions is {}'.format(self.privileges[i-1]))
#
#
# class Admin(User):
#     def __init__(self,first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges()
#
#
# admin = Admin('user', 'admin')
# admin.privileges.show_privileges(1)