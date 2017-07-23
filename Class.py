#!/usr/bin/env python2

class Employee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = name + '.' + last + '@patito.com'

    def fullname(self):
        return '{} {}'.format(self.name, self.last)

emp1 = Employee('Edson', 'Cervantes', 60000)
emp2 = Employee('Juan', 'Perez', 80000)

#Se puede mandar llamar a la clase con su funcion y al final invocar a la instancia
#O tambien se puede mandar llamar a la instancia junto con el metodo  
print Employee.fullname(emp1)
print emp2.fullname()
# emp1.name = "Edson"
# emp1.last = "Cervantes"
# emp1.email = "Edson.Cervantes@tygerdev.com"
# emp1.pay = 60000

# emp2.name = "Edson"
# emp2.last = "Cervantes"
# emp2.email = "Edson.Cervantes@tygerdev.com"
# emp2.pay = 60000

# print '{} {}'.format(emp1.name, emp1.last)
print emp1.email
print emp2.email
