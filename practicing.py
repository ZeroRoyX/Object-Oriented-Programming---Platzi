# class Employee:

#     raise_amount = 1.04
    
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#     def full_name(self):
#         # return self.first + ' ' + self.last
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)        

# emp_1 = Employee('Roy', 'Arana', 8000)
# emp_2 = Employee('Aracely', 'Rodriguez', 10000)
# emp_3 = Employee('Chester', 'Cheetos', 24000)

# print(emp_3.full_name())
# print(Employee.raise_amount)
# print(emp_3.raise_amount)
# emp_3.raise_amount = 1.6
# print(emp_3.raise_amount)
# print(emp_3.pay)
# emp_3.apply_raise()
# # Employee.apply_raise(emp_3)
# print(emp_3.pay)


class Empleado:

    numero_empleados = 0
    aumento = 1.04

    def __init__(self, nombre, apellido, pago, curp):
        self.nombre = nombre
        self.apellido = apellido
        self.pago = pago
        self.curp = curp

        Empleado.numero_empleados += 1

    def nombrecompleto(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def aplicar_aumento(self):
        self.pago = int(self.pago * self.aumento)

mirna = Empleado('Mirna', 'Rosas', 7200, 'AHE234')
leo = Empleado('Leonor', 'Gomez', 7200, 'AHE234')
chuy = Empleado('Jesus', 'Medina', 5000, 'AHE234')

print(mirna.pago)
print(leo.pago)
print(chuy.pago)
print(Empleado.aumento)
mirna.aplicar_aumento()
leo.aplicar_aumento()
chuy.aplicar_aumento()
print(mirna.pago)
print(leo.pago)
print(chuy.pago)