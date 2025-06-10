#!/usr/bin/python3
class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print (f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}"):

    def serialize(self, filename):
        with open(filename, "ab") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            data = pickle.load(f)
            return cls(data)