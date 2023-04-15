def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

def sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def average(student):
    return sum(student) / 4

def student_to_str(student):
    return "{}\t{}\t{}".format(
        student["name"],
        sum(student),
        average(student)
    )

students = [
    create_student("YJ", 100, 98, 88, 95),
    create_student("JY", 97, 88, 98, 100),
    create_student("AA", 98, 96, 100, 95),
    create_student("BB", 88, 100, 90, 86)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_str(student), sep="\t")
