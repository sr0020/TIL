class Student:

    # 클래스 변수
    count = 0
    students  = []

    @classmethod
    def print(cls):
        print("이름", "총점", "평균", sep="\t")
        for student in cls.students:
            print(str(student)) 

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def sum(self):
        return self.korean + self.math + self.english + self.science

    def average(self):
        return self.sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.sum(),
            self.average()
        )

Student("YJ", 100, 98, 88, 95)
Student("JY", 97, 88, 98, 100)
Student("AA", 98, 96, 100, 95)
Student("BB", 88, 100, 90, 86)

Student.print()
print(Student.count)