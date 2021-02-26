class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# En los parentesis ponemos de donde se hereda:
class Developer (Employee):
    raise_amount = 1.10 # Este solo aplica a los Developers
    # init para developers
    def __init__(self, first, last, pay, prog_lang): 
        # init de la clase padre, este para los employees y se trae instance variables.
        super().__init__(first, last, pay) 
        self.prog_lang = prog_lang


class Manager (Employee):
    def __init__(self, first, last, pay, employees=None): 
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        
 
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mike = Manager('Miguel', 'Arana', 90000, [dev_1])

print(mike.email)
mike.add_emp(dev_2)
mike.remove_emp(dev_1)
mike.print_emps()


# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email) 
