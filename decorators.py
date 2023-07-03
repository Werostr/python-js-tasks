from datetime import date


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def from_birth_year(cls, name, surname, birth_year):
        return cls(name, surname, date.today().year - birth_year)

    @property
    def fullname(self):
        return "{self.name} {self.surname}".format(self=self)


p1 = Person.from_birth_year("Wera", "Ostra", 2001)
print(p1.fullname)
