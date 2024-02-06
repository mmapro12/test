class Person:

    def __init__(self, name: str, surname: str, age: int, birthdate: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth_date = birthdate
    

    def define(self):
        return (f"{self.name.title()} {self.surname.title()} - {self.age} - {self.birth_date}")


person = Person("Muhammed", "Alnirabani", 15, 2009)
person.define()

