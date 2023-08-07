class Student():
    def __init__(self, age, sex, name, second_name, chromosomes, course, addition):
        self.age = age
        self.sex = sex
        self.name = name
        self.second_name = second_name
        self.chromosomes = chromosomes
        self.course = course
        self.admission_year = 2017
        self.addition = addition

student_1 = Student(21, 'female', 'Kris', 'Mira', 46, 2, 'Love')
student_2 = Student(20, 'male', 'Vova', 'Rusakov', 47, 2, 'Dolboeb suka')
student_3 = Student(18, 'male', 'Artem', 'Kosya', 46, 1, 'Pupsik')
student_4 = Student(19, 'male', 'Sergey', 'Belikov', 46, 2, 'Machine')
student_5 = Student(25, 'male', '2pac', 'Shakur', 46, 228, 'RIP(((')
print(student_1.addition)
print(student_2.chromosomes)
print(student_3.age)
print(student_4.admission_year)


