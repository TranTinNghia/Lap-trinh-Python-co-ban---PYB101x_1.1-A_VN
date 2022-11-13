# Hàm tinhtoan_diemtongket(): Tính điểm trung bình cho từng môn học của từng học sinh:
# Input là file "diem_chitiet.txt".
# Output là 1 dict: {"Mã học sinh" : {"Môn học" : Điểm trung bình}}.
def tinhtoan_diemtongket(file_name,so_hoc_sinh):
    with open(file_name) as f:
        for line in f: # Chạy qua từng dòng của f.
            diem_chitiet = dict()
            for ma_hoc_sinh in range(1,so_hoc_sinh): # Chạy vòng lặp từ vị trí 1 (là dòng có mã học sinh) đến độ dài của dữ liệu khi sử dụng hàm readlines trong hàm main().
                if line.startswith(str(ma_hoc_sinh) + ";"): # Xét dòng bắt đầu bằng mã học sinh và có dấu chấm phẩy ngay bên cạnh.
                    line = line.rstrip()
                    find_diem = line[(line.find(" ") + 1):] # Tìm vị trí của khoảng trắng đầu tiên, và lấy dữ liệu đến cuối của mỗi dòng.
                    list_diem = find_diem.split(";") # Tách điểm của từng môn học.
                    # Tách các điểm của một môn ra, đồng thời gán vào dict diem_chitiet, key là tên môn học:
                    diem_chitiet["Toan"] = list_diem[0].split(",")
                    diem_chitiet["Ly"] = list_diem[1].split(",")
                    diem_chitiet["Hoa"] = list_diem[2].split(",")
                    diem_chitiet["Sinh"] = list_diem[3].split(",")
                    diem_chitiet["Van"] = list_diem[4].split(",")
                    diem_chitiet["Anh"] = list_diem[5].split(",")
                    diem_chitiet["Su"] = list_diem[6].split(",")
                    diem_chitiet["Dia"] = list_diem[7].split(",")
                    for mon_hoc,diem_so in diem_chitiet.items(): # Key là biến mon_hoc, value là biến diem_so, từ dict diem_chitiet với cặp (mon_hoc,diem_so) là các tuple.
                        if (mon_hoc == "Toan") or (mon_hoc == "Ly") or (mon_hoc == "Hoa") or (mon_hoc == "Sinh"):
                            chuyen_doi = [float(i) for i in diem_so] # Ban đầu, giá trị của diem_so là string, phải chuyển thành float để tính trung bình.
                            # Tính điểm trung bình của 4 môn tự nhiên:
                            trung_binh = chuyen_doi[0] * 0.05 + chuyen_doi[1] * 0.1 + chuyen_doi[2] * 0.15 + chuyen_doi[3] * 0.7
                            # Gán điểm trung bình thay thế cho điểm chi tiết của 4 môn tự nhiên vào dict diem_chitiet, với key là mon_hoc:
                            diem_chitiet[mon_hoc] = round(trung_binh,2)
                        else:
                            chuyen_doi = [float(i) for i in diem_so]
                            # Tính điểm trung bình của 4 môn xã hội:
                            trung_binh = chuyen_doi[0] * 0.05 + chuyen_doi[1] * 0.1 + chuyen_doi[2] * 0.1 + chuyen_doi[3] * 0.15 + chuyen_doi[4] * 0.6
                            # Gán điểm trung bình thay thế cho điểm chi tiết của 4 môn xã hội vào dict diem_chitiet, với key là mon_hoc:
                            diem_chitiet[mon_hoc] = round(trung_binh,2)
                    diem_tongket[str(ma_hoc_sinh)] = diem_chitiet
        return diem_tongket

# Hàm luudiem_trungbinh(): Lưu điểm trung bình của từng học sinh vào 1 file txt:
# Input: Đường dẫn cho file ouput, dict điểm tổng kết.
# Output: File "diem_trungbinh.txt".
def luudiem_trungbinh(duong_dan_output,diem_tongket):
    with open(duong_dan_output,"w") as f:
        # Viết tiêu đề cho file "diem_trungbinh.txt":
        f.write("Ma HS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia\n")
        # Chạy vòng lặp để lấy ra mã học sinh và điểm chi tiết các môn học của từng học sinh:
        for ma_hs,diem_trung_binh in diem_tongket.items():
            f.write(str(ma_hs) + "; ") # Viết ra mã học sinh.
            for mon_hoc in diem_trung_binh:
                if mon_hoc == "Dia":
                    f.write(str(diem_trung_binh[mon_hoc])) # Nếu là môn địa thì ghi điểm trung bình vào nhưng không có dấu ";" ở cuối dòng theo đúng format của file "diem_chitiet.txt".
                else:
                    f.write(str(diem_trung_binh[mon_hoc]) + ";") # Viết ra điểm trung bình của từng môn, key là tên môn học, các điểm ngăn cách nhau bằng dấu ";".
            f.write("\n")

# Hàm main():
# Thực thi 2 hàm tinhtoan_diemtongket() và luudiem_trungbinh().
if __name__ == "__main__":
    file_name = "diem_chitiet.txt"
    diem_tongket = dict()
    duong_dan_output = "diem_trungbinh.txt"
    with open(file_name) as f:
        toan_bo_du_lieu = f.readlines()
        so_hoc_sinh = len(toan_bo_du_lieu)
    print(tinhtoan_diemtongket(file_name,so_hoc_sinh))
    luudiem_trungbinh(duong_dan_output,diem_tongket)



