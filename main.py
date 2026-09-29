class Student:
    def __init__(self, name: str, age: int, course: str):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self) -> None:
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"I am studying {self.course}.")


student = Student("Amna", 25, "Data Analytics")
student.introduce()
