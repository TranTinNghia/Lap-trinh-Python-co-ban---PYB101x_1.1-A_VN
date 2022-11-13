# Hàm xeploai_hocsinh():
# Phân loại học lực của từng học sinh theo điểm trung bình của từng môn và điểm trung bình chuẩn.
# Ouput là 1 dict: {"Mã học sinh" : "Phân loại học lực"}.
def xeploai_hocsinh(file_name,so_hoc_sinh):
    with open(file_name,"r") as f: # Mở file "diem_trungbinh.txt".
        for line in f: # Chạy từng dòng trong file "diem_trungbinh.txt".
            for ma_hoc_sinh in range(1,so_hoc_sinh): # Chạy vòng lặp từ vị trí 1 (là dòng có mã học sinh) đến độ dài của dữ liệu khi sử dụng hàm readlines trong hàm main().
                if line.startswith(str(ma_hoc_sinh) + ";"): 
                    line = line.rstrip()
                    find_diem = line[(line.find(" ") + 1):] # Tìm vị trí của khoảng trắng đầu tiên, và lấy dữ liệu đến cuối của mỗi dòng.
                    list_diem = find_diem.split(";") # Tạo ra list điểm trung bình chứa điểm trung bình cho từng môn của từng học sinh. 
                    for i in list_diem:
                        # Tính điểm trung bình chuẩn:
                        diem_trungbinh_chuan = ((float(list_diem[0]) + float(list_diem[4]) + float(list_diem[5])) * 2 + (float(list_diem[1]) + float(list_diem[2]) + float(list_diem[3]) + float(list_diem[6]) + float(list_diem[7])) * 1) / 11
                        diem_trungbinh_chuan = round(diem_trungbinh_chuan,2)
                        # Đánh giá học lực theo điểm trung bình của từng môn và điểm trung bình chuẩn:
                        if (float(i) >= 8.0) and diem_trungbinh_chuan > 9.0:
                            xeploai_diem_trungbinh_chuan[str(ma_hoc_sinh)] = "Xuat sac"
                        elif float(i) >= 6.5 and diem_trungbinh_chuan > 8.0:
                            xeploai_diem_trungbinh_chuan[str(ma_hoc_sinh)] = "Gioi"
                        elif float(i) >= 5.0 and diem_trungbinh_chuan > 6.5:
                            xeploai_diem_trungbinh_chuan[str(ma_hoc_sinh)] = "Kha"
                        elif float(i) >= 4.5 and diem_trungbinh_chuan > 6.0:
                            xeploai_diem_trungbinh_chuan[str(ma_hoc_sinh)] = "Trung binh kha"
                        else:
                            xeploai_diem_trungbinh_chuan[str(ma_hoc_sinh)] = "Trung binh"
    return xeploai_diem_trungbinh_chuan

# Hàm xeploai_thidaihoc_hocsinh():
# Phân loại theo tổng điểm trung bình của từng khối thi cho từng học sinh.
# Output: {"Mã học sinh" : [Phân loại theo khối thi đại học]}.
def xeploai_thidaihoc_hocsinh(file_name,so_hoc_sinh):
    with open(file_name,"r") as f: # Mở file "diem_trungbinh.txt".
        for line in f: # Chạy từng dòng trong file "diem_trungbinh.txt".
            for ma_hoc_sinh in range(1,so_hoc_sinh): # Chạy vòng lặp từ vị trí 1 (là dòng có mã học sinh) đến độ dài của dữ liệu khi sử dụng hàm readlines trong hàm main().
                if line.startswith(str(ma_hoc_sinh) + ";"):
                    line = line.rstrip()
                    find_diem = line[(line.find(" ") + 1):] # Tìm vị trí của khoảng trắng đầu tiên, và lấy dữ liệu đến cuối của mỗi dòng.
                    list_diem = find_diem.split(";") # Tạo ra list điểm trung bình chứa điểm trung bình cho từng môn của từng học sinh. 
                    list_tongdiem_khoithidaihoc = list() # Tạo list rỗng, dùng để lưu giá trị tổng điểm trung bình của các khối thi đại học.
                    for i in list_diem: # Chạy vòng lặp qua list điểm trung bình.
                        # Tính điểm trung bình của từ khối thi đại học:
                        # Khối A: Toán, Lý, Hoá.
                        # Khối A1: Toán, Lý, Anh.
                        # Khối B: Toán, Hoá, Sinh.
                        # Khối C: Văn, Sử, Địa.
                        # Khối D: Toán, Văn, Anh.
                        tongdiem_khoi_A = round((float(list_diem[0]) + float(list_diem[1]) + float(list_diem[2])),2)
                        tongdiem_khoi_A1 = round((float(list_diem[0]) + float(list_diem[1]) + float(list_diem[5])),2)
                        tongdiem_khoi_B = round((float(list_diem[0]) + float(list_diem[2]) + float(list_diem[3])),2)
                        tongdiem_khoi_C = round((float(list_diem[4]) + float(list_diem[6]) + float(list_diem[7])),2)
                        tongdiem_khoi_D = round((float(list_diem[0]) + float(list_diem[4]) + (float(list_diem[5]))*2),2)
                    # Lưu điểm vào list rỗng.
                    list_tongdiem_khoithidaihoc.append(tongdiem_khoi_A)
                    list_tongdiem_khoithidaihoc.append(tongdiem_khoi_A1)
                    list_tongdiem_khoithidaihoc.append(tongdiem_khoi_B)
                    list_tongdiem_khoithidaihoc.append(tongdiem_khoi_C)
                    list_tongdiem_khoithidaihoc.append(tongdiem_khoi_D)
                    list_phanloai_nangluc = list() # Tạo list rỗng, dùng để phân loại tổng điểm của từng học sinh theo từng khối thi đại học.
                    # Phân loại theo khối tự nhiên (A, A1, B).
                    for diem_khoi_tu_nhien in list_tongdiem_khoithidaihoc[0:3]:
                        if diem_khoi_tu_nhien >= 24:
                            list_phanloai_nangluc.append(1)
                        elif (diem_khoi_tu_nhien >= 18) and (diem_khoi_tu_nhien < 24):
                            list_phanloai_nangluc.append(2)
                        elif (diem_khoi_tu_nhien >= 12) and (diem_khoi_tu_nhien < 18):
                            list_phanloai_nangluc.append(3)
                        else:
                            list_phanloai_nangluc.append(4)
                    # Phân loại theo khối xã hội (C).
                    for diem_khoi_xa_hoi in list_tongdiem_khoithidaihoc[3:4]:
                        if diem_khoi_xa_hoi >= 21:
                            list_phanloai_nangluc.append(1)
                        elif (diem_khoi_xa_hoi >= 15) and (diem_khoi_xa_hoi < 21):
                            list_phanloai_nangluc.append(2)
                        elif (diem_khoi_xa_hoi >= 12) and (diem_khoi_xa_hoi < 15):
                            list_phanloai_nangluc.append(3)
                        else:
                            list_phanloai_nangluc.append(4)
                    # Phân loại theo khối cơ bản (D).
                    for diem_khoi_co_ban in list_tongdiem_khoithidaihoc[4:]:
                        if diem_khoi_co_ban >= 32:
                            list_phanloai_nangluc.append(1)
                        elif (diem_khoi_co_ban >= 24) and (diem_khoi_co_ban < 32):
                            list_phanloai_nangluc.append(2)
                        elif (diem_khoi_co_ban >= 20) and (diem_khoi_co_ban < 24):
                            list_phanloai_nangluc.append(3)
                        else:
                            list_phanloai_nangluc.append(4)
                    # Ghi value của list xeploai_diemthidaihoc() với key là mã học sinh.
                    xeploai_diemthidaihoc[str(ma_hoc_sinh)] = list_phanloai_nangluc
    return xeploai_diemthidaihoc

# Hàm main():
# Thực thi 2 hàm xeploai_hocsinh() và xeploai_thidaihoc_hocsinh(), đồng thời ghi kết quả ra file "danhgia_hocsinh.txt".
# Output là file "danhgia_hocsinh.txt", với format giống với file "diem_chitiet.txt" như đề bài cho ban đầu.                         
if __name__ == "__main__": 
    file_name = "diem_trungbinh.txt"
    with open(file_name,"r") as f: # Mở file "diem_trungbinh.txt".
        toan_bo_du_lieu = f.readlines() # Ghi toàn bộ dữ liệu của file "diem_trungbinh.txt" vào cùng một dòng, và tạo ra 1 list dữ liệu.
        so_hoc_sinh = len(toan_bo_du_lieu) # Tính độ dài của list vừa tạo thành.
    xeploai_diem_trungbinh_chuan = dict() # Tạo dict rỗng, dùng để lưu giá trị của hàm xeploai_hocsinh().
    xeploai_diemthidaihoc = dict() # Tạo dict rỗng, dùng để lưu giá trị của hàm xeploai_thidaihoc_hocsinh().
    print(xeploai_hocsinh(file_name,so_hoc_sinh)) # In giá trị của hàm xeploai_hocsinh().
    print(xeploai_thidaihoc_hocsinh(file_name,so_hoc_sinh)) # In giá trị của hàm xeploai_thidaihoc_hocsinh().
    temporary_dict = dict() # Tạo dict tạm rỗng, với key là mã học sinh và value là 1 list (Gồm xếp loại Xuất sắc, Giỏi, Khá, Trung bình Khá hoặc Trung bình và phân loại tổng điểm trung bình theo từng khối thi đại học).
    for ma_hs in xeploai_diem_trungbinh_chuan.keys():
        temporary_list = list() # Tạo list tạm rỗng, dùng để lưu giá trị về Xếp loại Xuất sắc, Giỏi, Khá, Trung bình Khá hoặc Trung bình và phân loại tổng điểm trung bình theo từng khối thi đại học.
        temporary_list.append(xeploai_diem_trungbinh_chuan[ma_hs]) # Gán giá trị Xếp loại Xuất sắc, Giỏi, Khá, Trung bình Khá hoặc Trung bình vào list tạm rỗng, với key là mã học sinh, lấy từ dict xeploai_diem_trungbinh_chuan().
        temporary_list.extend(xeploai_diemthidaihoc[ma_hs]) # Gán giá trị Phân loại tổng điểm trung bình theo từng khối thi đại học vào list tạm rỗng, với key là mã học sinh, lấy từ dict xeploai_diemthidaihoc().
        temporary_dict[ma_hs] = temporary_list # Gán giá trị của list tạm rỗng vào dict tạm rỗng, với key là mã học sinh.
    # print(temporary_dict)
    duongdan_output = "danhgia_hocsinh.txt"
    f_output = open(duongdan_output,"w") # Tạo mới file "danhgia_hocsinh.txt", nếu có rồi thì ghi đè giá trị vào file.
    f_output.write("Ma HS, Xeploai_TB_chuan, Xeploai_A, Xeploai_A1, Xeploai_B, Xeploai_C, Xeploai_D\n") # Ghi dòng tiêu đềvà xuống dòng.
    for k in temporary_dict.keys(): # Chạy vòng lặp qua các key (mã học sinh) của dict tạm.
        f_output.write(str(k) + "; ") # Ghi giá trị mã học sinh vào file.
        # Chạy vòng lặp qua value của dict tạm. Độ dài value của dict tạm là 6.
        # Xét biến m = 0 ban đầu, nếu chạy qua từng giá trị trong value của dict tạm, sẽ cộng 1 vào m.
        # Nếu m khác 6 thì ghi giá trị vào file, các giá trị ngăn cách nhau bằng ";".
        # Cho đến khi m = 6, ghi giá trị vào file và xuống dòng. 
        m = 0  
        for n in temporary_dict[k]:
            m = m + 1
            if m != 6:
                f_output.write(str(n) + "; ")
            else:
                f_output.write(str(n) + "\n")



