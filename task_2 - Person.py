from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"Student's name: {self.name}, yob: {self.yob}, grade: {self.grade}"


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor's name: {self.name}, yob: {self.yob}, specialist: {self.specialist}"


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"Teacher's name: {self.name}, yob: {self.yob}, subject: {self.subject}"


class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        description = f"Ward: {self.name}\n"
        if self.people:
            description += "\n".join([person.describe()
                                     for person in self.people])
        else:
            description += "No people in this ward."
        return description

    def count_doctor(self):
        dem = 0
        for _ in self.people:
            if isinstance(Person, Doctor):
                dem += 1
        return dem

    def sort_age(self):
        return self.people.sort(key=lambda person: person.yob)

    def compute_average(self):
        total_yob = 0
        teacher_count = 0
        for person in self.people:
            if isinstance(Person, Teacher):
                total_yob += person.yob
                teacher_count += 1
        if teacher_count == 0:
            return None
        return total_yob // teacher_count


ward = Ward("Ward 1")

student1 = Student("John", 2004, "second year uni")
print(student1.describe())

doc1 = Doctor("Wick", 1960, "digestive system")
print(doc1.describe())

ward.add_person(Student("Alice", 2005, "10th Grade"))
ward.add_person(Teacher("Mr. Smith", 1980, "Mathematics"))
ward.add_person(Teacher("Mr. Kevin", 1975, "Geographics"))
ward.add_person(Doctor("Dr. Brown", 1995, "Cardiology"))
ward.add_person(Doctor("Dr. Harry", 1985, "Cancers"))
print(ward.describe())
print(f"\nthe number of doctor in {ward.name} is {ward.count_doctor()}")

ward.sort_age()

print("\nsorting by age: ")
print(ward.describe())
print(f"\nthe average age of teachers is {ward.compute_average()}")
