class Student:    
    def __init__(self, student_name, diem_trung_binh):
        self.student_name = student_name
        self.diem_trung_binh = round((sum((float(j) for j in diem_trung_binh.split()))/3),2)
    def print_diem_trung_binh(self):
        print("The average mark of {0} is {1}".format(self.student_name, self.diem_trung_binh))

program_object = Student(input("Nhập tên học sinh: "), input("Nhập điểm 3 môn của học sinh: "))
program_object.print_diem_trung_binh()