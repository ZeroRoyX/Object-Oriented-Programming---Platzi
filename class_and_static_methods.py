class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    ### CREATING NEW OBJECTS USING CLASS METHOD
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # Static Method using dates
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Employee.set_raise_amt(1.10)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.apply_raise()
# emp_2.apply_raise()

# print(emp_1.pay)
# print(emp_2.pay)

### CREATING NEW OBJECTS USING CLASS METHODS

# emp_str_3 = 'John-Doe-70000'
# emp_str_4 = 'Steve-Smith-30000'
# emp_str_5 = 'Jane-Doe-90000'

# # first, last, pay = emp_str_3.split('-')
# # print(first, last, pay)

# # emp_3 = Employee(first, last, pay)
# # print(emp_3.email)
# # print(emp_3.pay)

# emp_4 = Employee.from_string(emp_str_4)
# print(emp_4.email)
# print(emp_4.pay)

### STATIC METHOD

import datetime
my_date = datetime.date(2021, 2, 21)

print(Employee.is_workday(my_date))
print(my_date)
