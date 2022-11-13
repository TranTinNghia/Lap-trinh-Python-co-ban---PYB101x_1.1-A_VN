class Nhanvien:
    def __init__(self, name, month, salary_per_day, day_of_working, coefficient):
        self.ten_quan_ly = name
        self.thang = month
        self.luong_co_ban = salary_per_day
        self.so_ngay_lam_viec = day_of_working
        self.he_so_luong = coefficient
    def tinh_luong(self):
        luong_tong_chua_thuong = self.luong_co_ban * self.so_ngay_lam_viec * self.he_so_luong - 1000000
        if luong_tong_chua_thuong > 9000000:
            luong_nhan_chua_thuong = luong_tong_chua_thuong * 90 / 100
        else:
            luong_nhan_chua_thuong = luong_tong_chua_thuong
        return luong_nhan_chua_thuong
    def hien_thi_luong(self):
        return "Luong cua nhan vien {0} nhan duoc trong thang {1} la: {2} VND.".format(self.ten_quan_ly, int(self.thang), int(QuanLy.tinh_luong_thuc_nhan(self)))
class QuanLy(Nhanvien):
    def __init__(self, name, month, salary_per_day, day_of_working, coefficient, performance):
        super().__init__(name, month, salary_per_day, day_of_working, coefficient)
        self.he_so_hieu_qua = performance
        self.he_so_thuong = self.he_so_hieu_qua - 1
    def tinh_luong_thuc_nhan(self):
        luong_khong_thuong = self.tinh_luong()
        if self.he_so_hieu_qua < 1:
            luong_thuc_nhan = luong_khong_thuong * self.he_so_hieu_qua
        else:
            luong_thuong = (self.luong_co_ban * self.so_ngay_lam_viec * self.he_so_luong - 1000000) * self.he_so_thuong * 85 / 100
            luong_thuc_nhan = luong_khong_thuong + luong_thuong
        return luong_thuc_nhan
ten_quan_ly = input("Nhập tên của người quản lý: ")
thong_tin = input("Nhập thông tin để tính lương cho người quản lý: ").split(" ")
a = QuanLy(ten_quan_ly,float(thong_tin[0]),float(thong_tin[1]),float(thong_tin[2]),float(thong_tin[3]),float(thong_tin[4]))
print(a.hien_thi_luong())
