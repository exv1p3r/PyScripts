#!/usr/bin python2

class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@tydev.com'
        
        Employee.num_of_emp += 1

                

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Edson', 'Cervantes', 60000)
emp2 = Employee('Juan', 'Perez', 40000)

print Employee.apply_raise(emp1)

print Employee.fullname(emp1)



# print Employee.__dict__
# print Employee.__doc__
# print emp1
# print emp2

# emp1.first = "Edson"
# emp1.last = "Cervantes"
# emp1.email = 'edson.cervantes@tydev.com'
# emp1.pay = 60000


# emp2.first = "Juan"
# emp2.last = "Perez"
# emp2.email = 'juan.perez@tydev.com'
# emp2.pay = 40000

# print emp1.first
# print emp2.first