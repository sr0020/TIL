class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def sum(self):
        return self.korean + self.math + self.english + self.science

    def average(self):
        return self.sum() / 4

    def to_str(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.sum(),
            self.average()
        )

students = [
    Student("YJ", 100, 98, 88, 95),
    Student("JY", 97, 88, 98, 100),
    Student("AA", 98, 96, 100, 95),
    Student("BB", 88, 100, 90, 86)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_str(), sep="\t") 
