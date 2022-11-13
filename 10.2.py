class Nhanvien:
    def __init__(self, name_of_employee, month, salary_per_day, day_of_working, coefficient):
        self.name = name_of_employee
        self.month = month
        self.salary_per_day = salary_per_day
        self.working_day = day_of_working
        self.coefficient = coefficient
    def tinh_luong(self):
        total_luong = self.salary_per_day * self.working_day * self.coefficient - 1000000
        if total_luong > 9000000:
            total_luong = (total_luong * 90) / 100
        else:
            total_luong = total_luong     
        return total_luong
    def hien_thi_luong(self):
        print("Luong cua nhan vien {0} nhan duoc trong thang {1} là: {2} VND.".format(self.name, int(self.month), int(Nhanvien.tinh_luong(self))))
ten_nhan_vien = input("Nhập tên nhân viên: ")
thong_tin = input("Nhập thông tin để tính lương cho nhân viên: ").split(", ")
a = Nhanvien(ten_nhan_vien,float(thong_tin[0]),float(thong_tin[1]),float(thong_tin[2]),float(thong_tin[3]))
a.hien_thi_luong()