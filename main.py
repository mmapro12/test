print("Welcome to DATAPY")

class Person:

    def __init__(self, name: str, surname: str, age: int, birthdate: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth_date = birthdate

    def define(self):
        return f"{self.name.title()} {self.surname.title()} - {self.age} - {self.birth_date}"

    def set_data(self, **kwargs):
        for key, value in kwargs.items():
            match key:
                case "name":
                    self.name = value
                case "surname":
                    self.surname = value
                case "age":
                    self.age = value
                case "birth_day":
                    self.birth_date = value


person = Person("Muhammed", "Alnirabani", 15, 2009)
print(person.define())

person.set_data(name="Ahmed", age=31)
print(person.define())
