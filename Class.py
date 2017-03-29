class Employee:
    def __init__(self, name, lastname, pay):
        self.name = name
        self.lastname = lastname
        self.pay = pay
        self.email = name + "." + lastname + "@patito.corp"

    def fullname(self):
        return "{} {}".format(self.name, self.lastname)

emp1 = Employee('Edson', 'Cervantes', 5000)
print emp1.email
print emp1.pay

emp2 = Employee('Usuario', 'Prueba', 7000)
print emp2.email
print emp2.name

print emp1.fullname()

print Employee.fullname(emp2)

#print emp1
#print emp2

#emp1.name = "Edson"
#emp1.lastname = "Cervantes"
#emp1.email = "edsoncervantes90@gmail.com"
#emp1.pay = "5000"

#print emp1.name + "\t" + emp1.lastname