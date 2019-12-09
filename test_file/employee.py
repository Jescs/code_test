class Employee():
    def __init__(self,first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, prove=5000):
        self.salary += prove
        print('{} {}\'s salary is {}'.format(self.first, self.last, self.salary))
        return self.salary
