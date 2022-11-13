import urllib.request
import json
import xml.etree.ElementTree as ET
import ssl
import sys

# Class Employee:
class Employee:
    def __init__(self, id, name, salary_base, working_days, department, working_performance, bonus, late_coming_days):
        self.ID_nhan_vien = id
        self.ten_nhan_vien = name
        self.he_so_luong = salary_base
        self.so_ngay_lam_viec = working_days
        self.bo_phan = department
        self.he_so_hieu_qua = working_performance
        self.thuong = bonus
        self.so_ngay_di_muon = late_coming_days
        self.tong_thu_nhap_chua_thuong = (self.he_so_luong * self.so_ngay_lam_viec) * self.he_so_hieu_qua

# Class Department:
class Department:
    def __init__(self, id, bonus_salary):
        self.ma_bo_phan = id
        self.thuong_bo_phan = bonus_salary
    def get_department(self):
        return self.ma_bo_phan
    def get_bonus_salary(self):
        return self.thuong_bo_phan

# Class Manager:
class Manager(Employee):
    def __init__(self, id, name, salary_base, working_days, department, working_performance, bonus, late_coming_days):
        super().__init__(id, name, salary_base, working_days, department, working_performance, bonus, late_coming_days)

# Hàm hiển thị danh sách nhân viên:
def hien_thi_nhan_vien(data_nhan_vien):
    for dict_nhan_vien in data_nhan_vien:
        print("\n----------------\n")
        for k,v in dict_nhan_vien.items():
            if k == "Hệ số lương" or k == "Thưởng":
                v = "{:,} (VNĐ)".format(int(v))
                print("{0}: {1}".format(k,v))
            elif k == "Số ngày làm việc" or k == "Số ngày đi muộn":
                print("{0}: {1} (ngày)".format(k,v))
            else:
                print("{0}: {1}".format(k,v))
    print("\n------------------\n")

# Hàm hiển thị danh sách bộ phận:
def hien_thi_bo_phan(data_bo_phan):
    for k,v in data_bo_phan.items():
        print("-----")
        print("{0}: {1}".format("Mã bộ phận", k))
        print("Thưởng bộ phận: {:,} (VNĐ)".format(v))
    print("-----")

# Hàm thêm nhân viên mới:
def them_nhan_vien_moi(data_nhan_vien, data_bo_phan):
    
    print("-----")
    print("Thêm nhân viên mới ...")

    # Nhập mã nhân viên mới:
    while True:
        ma_nhan_vien_moi = input("Nhập mã số: ")
        # Thông tin không được để trống, bắt buộc phải nhập vào:
        if ma_nhan_vien_moi == "":
            print("Bạn không được bỏ trống thông tin này!")
        # Check xem mã nhân viên mới nhập vào đã tồn tại hay chưa:
        elif any(ma_nhan_vien_moi in dict_nhan_vien["Mã số"] for dict_nhan_vien in data_nhan_vien):
            print("Mã nhân viên đã tồn tại!")
        else:
            break

    # Nhập mã bộ phận cho nhân viên mới:
    while True:    
        ma_bo_phan_nhan_vien_moi = input("Nhập mã bộ phận: ")
        # Thông tin không được để trống, bắt buộc phải nhập vào:
        if ma_bo_phan_nhan_vien_moi == "":
            print("Bạn không được bỏ trống thông tin này!")
        # Check xem mã bộ phận mới nhập vào đã tồn tại hay chưa, nếu chưa tồn tại thì tạo mới:
        elif any(ma_bo_phan_nhan_vien_moi in ma_bo_phan_moi for ma_bo_phan_moi in data_bo_phan) == False:
            print("Mã bộ phận chưa tồn tại, tạo mới ...")
            while True:
                thuong_bo_phan_moi = input("Nhập thưởng bộ phận: ")   
                if thuong_bo_phan_moi == "":
                    print("Bạn không được bỏ trống thông tin này!")
                elif not thuong_bo_phan_moi.isnumeric():
                    print("Bạn phải nhập một số dương!")
                else:
                    break
            print("Đã tạo bộ phận mới")
            data_bo_phan[ma_bo_phan_nhan_vien_moi] = int(thuong_bo_phan_moi)
            # Mở file "bo_phan.json", đọc và ghi nhằm ghi dữ liệu bộ phận mới thêm vào:
            f_bo_phan = open("bo_phan.json","w")
            json.dump(data_bo_phan,f_bo_phan,ensure_ascii = False, indent = 4)
            f_bo_phan.close()
            break
        else:     
            break        

    # Nhập chức vụ cho nhân viên mới:
    while True:
        chuc_vu = input("Nhập chức vụ (Quản lý / Nhân viên): ")
        if chuc_vu == "":
            print("Bạn không được bỏ trống thông tin này!")
        elif (chuc_vu != "Nhân viên") and (chuc_vu != "Quản lý"):
            print("Thông tin nhập vào không hợp lệ, vui lòng nhập lại!")
        elif ((chuc_vu == "Nhân viên") and ma_nhan_vien_moi[0:2] == "QL") or ((chuc_vu == "Quản lý") and ma_nhan_vien_moi[0:2] == "NV"):
            print("Mã nhân viên và chức vụ không khớp, vui lòng kiểm tra lại!")
        else:
            break 

    # Nhập họ và tên của nhân viên mới:
    while True:
        ho_va_ten = input("Nhập họ và tên: ")
        if ho_va_ten == "":
            print("Bạn không được bỏ trống thông tin này!")
        else:
            break

    # Nhập hệ số lương cho nhân viên mới:
    while True:    
        try:
            he_so_luong_moi = input("Nhập hệ số lương: ")
            if he_so_luong_moi == "":
                print("Bạn không được bỏ trống thông tin này!")
            elif (int(he_so_luong_moi) < 0) or (he_so_luong_moi.isalpha()):
                print("Bạn phải nhập một số dương!")
            else:
                he_so_luong_moi = int(he_so_luong_moi)
                break
        except:
            print("Bạn phải nhập một số dương!")
            continue

    # Nhập số ngày làm việc cho nhân viên mới:
    while True:
        try:
            so_ngay_lam_viec_moi = input("Nhập số ngày làm việc: ")
            if so_ngay_lam_viec_moi == "":
                print("Bạn không được bỏ trống thông tin này!")
            elif (int(so_ngay_lam_viec_moi) < 0) or (so_ngay_lam_viec_moi.isalpha()):
                print("Bạn phải nhập một số dương!")
            else:
                so_ngay_lam_viec_moi = int(so_ngay_lam_viec_moi)
                break
        except:
            print("Bạn phải nhập một số dương!")
            continue
        
    # Nhập hệ số hiệu quả cho nhân viên mới:
    while True:
        try:
            he_so_hieu_qua_moi = input("Nhập hệ số hiệu quả: ")
            if he_so_hieu_qua_moi == "":
                print("Bạn không được bỏ trống thông tin này!")
            elif (float(he_so_hieu_qua_moi) < 0) or (he_so_hieu_qua_moi.isalpha()):
                print("Bạn phải nhập một số dương!")
            else:
                he_so_hieu_qua_moi = float(he_so_hieu_qua_moi)
                break
        except:
            print("Bạn phải nhập một số dương!")
            continue

    # Nhập thưởng cho nhân viên mới:
    while True:
        try:
            thuong_moi = input("Nhập thưởng: ")
            if thuong_moi == "":
                print("Bạn không được bỏ trống thông tin này!")
            elif (int(thuong_moi) < 0) or (thuong_moi.isalpha()):
                print("Bạn phải nhập một số dương!")
            else:
                thuong_moi = int(thuong_moi)
                break
        except:
            print("Bạn phải nhập một số dương!")
            continue

    # Nhập số ngày đi muộn:
    while True:
        try:
            so_ngay_di_muon_moi = input("Nhập số ngày đi muộn: ")
            if so_ngay_di_muon_moi == "":
                print("Bạn không được bỏ trống thông tin này!")
            elif (int(so_ngay_di_muon_moi) < 0) or (so_ngay_di_muon_moi.isalpha()):
                print("Bạn phải nhập một số dương!")
            else:
                so_ngay_di_muon_moi = int(so_ngay_di_muon_moi)
                break
        except:
            print("Bạn phải nhập một số dương!")
            continue
    
    # Mở file "nhan_vien.json", đọc và ghi nhằm ghi dữ liệu nhân viên mới thêm vào:
    dict_nhan_vien_moi = {
        "Mã số" : ma_nhan_vien_moi,
        "Mã bộ phận" : ma_bo_phan_nhan_vien_moi,
        "Chức vụ" : chuc_vu,
        "Họ và tên" : ho_va_ten,
        "Hệ số lương" : he_so_luong_moi,
        "Số ngày làm việc" : so_ngay_lam_viec_moi,
        "Hệ số hiệu quả" : he_so_hieu_qua_moi,
        "Thưởng" : thuong_moi,
        "Số ngày đi muộn" : so_ngay_di_muon_moi}
    print("Đã thêm nhân viên mới!")
    print("-----")
    data_nhan_vien.append(dict_nhan_vien_moi)
    f_nhan_vien = open("nhan_vien.json","w", encoding = "utf-8")
    json.dump(data_nhan_vien,f_nhan_vien,ensure_ascii = False, indent = 4)
    f_nhan_vien.close()

# Hàm xoá nhân viên theo ID:
def xoa_nhan_vien_theo_ID(data_nhan_vien):
    print("-----")
    while True:
        a = len(data_nhan_vien) # Chiều dài của data_nhan_vien.
        id_nhan_vien_remove = input("Nhập mã nhân viên muốn xoá: ")
        for i in data_nhan_vien:
            j = i["Mã số"]
            if id_nhan_vien_remove == j:
                data_nhan_vien.pop(data_nhan_vien.index(i)) # Xoá thông tin nhân viên tại vị trí mà mã nhân viên nhập vào bằng đúng mã nhân viên có trong data_nhan_vien.
            elif id_nhan_vien_remove == "":
                a = a - 1 # Nếu bỏ qua không nhập mã nhân viên muốn xoá, vòng lặp sẽ trừ dần cho chiều dài data_nhan_vien về 0 thì sẽ ngừng. 
        b = len(data_nhan_vien) # Chiều dài của data_nhan_vien.
        # Nếu không nhập mã nhân viên muốn xoá, a < b, vì a sẽ bị trừ dần về 0 (như đã nói ở trên), trong khi b là chiều dài của data_nhan_vien luôn lớn hơn 0.
        # Nếu nhập mã nhân viên không nằm trong data_nhan_vien, vòng lặp for ở trên sẽ không làm ảnh hưởng đến a, nghĩa là a = b.
        # Nếu nhập mã nhân viên nằm trong data_nhan_vien, thông tin nhân viên đó sẽ bị xoá đi, và b sẽ bị trừ đi 1, trong khi a là chiều dài ban đầu của data_nhan_vien, nghĩa là a > b.
        if a > b:
            # Ghi thông tin lại, sau khi xoá nhân viên vào file "nhan_vien.json":
            f_nhan_vien = open("nhan_vien.json","w", encoding = "utf-8")
            json.dump(data_nhan_vien, f_nhan_vien, ensure_ascii = False, indent = 4)
            f_nhan_vien.close()
            print("Đã xoá nhân viên thành công!")
            print("-----")
            break
        elif a == b:
            print("Mã nhân viên không tồn tại!")
        else:
            print("Bạn không được bỏ trống thông tin này!")

# Hàm xoá bộ phận theo ID:
# Một lưu ý: Không thể xoá bộ phận trong khi mã nhân viên đang tồn tại.
def xoa_bo_phan_theo_ID(data_nhan_vien, data_bo_phan):
    print("-----")
    while True:
        try:
            # Tạo list chứa danh sách các mã bộ phận có trong file "nhan_vien.json", các dữ liệu không bị trùng lặp:
            temporary_list = list()
            for i in data_nhan_vien:
                temporary_list.append(i["Mã bộ phận"])
            list_chua_ma_bo_phan_nhan_vien_json = list(set(temporary_list))

            # Check mã nhân viên có đang tồn tại tương ứng với mã bộ phận muốn xoá hay không và thực hiện các bước xoá bộ phận:
            id_bo_phan_remove = input("Nhập mã bộ phận muốn xoá: ")
            a = len(list_chua_ma_bo_phan_nhan_vien_json) # Chiều dài của list chứa danh sách các mã bộ phận có trong file "nhan_vien.json".
            for j in list_chua_ma_bo_phan_nhan_vien_json:
                if id_bo_phan_remove == j:
                    a = a - 1
                else: 
                    a = a
            b = len(list_chua_ma_bo_phan_nhan_vien_json) # Chiều dài của list chứa danh sách các mã bộ phận có trong file "nhan_vien.json".
            # Nếu nhập mã bộ phận có tồn tại và có trong file "nhan_vien.json", điều đó nghĩa là có mã nhân viên tương ứng của mã bộ phận cần xoá đó, do đó chiều dài của list bị trừ đi 1, đồng nghĩa với a < b, không thể xoá bộ phận đi vì mã nhân viên tồn tại.
            # Nếu nhập mã bộ phận không tồn tại, trả về except.
            # Nếu nhập mã bộ phận có tồn tại nhưng không có trong file "nhan_vien.json", điều đó nghĩa là không có mã nhân viên tương ứng của mã bộ phận cần xoá đó, do đó chiều dài của list vẫn được giữ nguyên, đồng nghĩa luôn luôn xảy ra a = b và sẽ xoá được bộ phận.
            if id_bo_phan_remove == "":
                print("Bạn không được bỏ trống thông tin này!")
            elif a < b:
                print("Bạn không thể xoá bộ phận có nhân viên!")
            else:
                del data_bo_phan[id_bo_phan_remove]
                f_bo_phan = open("bo_phan.json","w")
                json.dump(data_bo_phan, f_bo_phan, ensure_ascii = False, indent = 4)
                f_bo_phan.close()
                print("Đã xoá bộ phận thành công!")
                print("-----")
                break
        except:
            print("Mã bộ phận không tồn tại!")
            continue          

# Hàm sửa thông tin nhân viên:
def sua_nhan_vien(data_nhan_vien, data_bo_phan):
    print("-----")
    print("Chỉnh sửa nhân viên\n")
    # Tạo list chứa danh sách mã nhân viện hiện có trong data_nhan_vien:
    list_ma_nhan_vien = [i["Mã số"] for i in data_nhan_vien]
    # Tạo dictionary chứa thông tin chỉnh sửa:
    new_dict_nhan_vien = {
        "Mã số" : None,
        "Mã bộ phận" : None,
        "Chức vụ" : None,
        "Họ và tên" : None,
        "Hệ số lương" : None,
        "Số ngày làm việc" : None,
        "Hệ số hiệu quả" : None,
        "Thưởng" : None,
        "Số ngày đi muộn" : None
    }
    # Check xem nhân viên nhập vào có tồn tại không:
    while True:
        ma_nhan_vien_can_sua = input("Nhập mã nhân viên: ")
        if any(ma_nhan_vien_can_sua in j for j in list_ma_nhan_vien) == False:
            print("Nhân viên không tồn tại!")
            continue
        elif ma_nhan_vien_can_sua == "":
            print("Bạn không được bỏ trống thông tin này!")
        else:
            break

    # Nếu mã nhân viên nhập vào có tồn tại, thực hiện các bước chỉnh sửa như bên dưới:
    for k in range(len(data_nhan_vien)):
        if ma_nhan_vien_can_sua == list_ma_nhan_vien[k]:
            new_dict_nhan_vien["Mã số"] = ma_nhan_vien_can_sua
            
            # Chỉnh sửa mã bộ phận:
            while True:
                ma_bo_phan_sua = input("Nhập mã bộ phận: ")
                # Nếu mã bộ phận không đổi, giữ nguyên giá trị từ data_nhan_vien:
                if ma_bo_phan_sua == "":
                    new_dict_nhan_vien["Mã bộ phận"] = data_nhan_vien[k]["Mã bộ phận"]
                    break
                # Nếu mã bộ phận thay đổi, check xem mã bộ phận nhập vào đã tồn tại chưa, nếu chưa thì nhập lại, nếu có thì thay đổi:
                else:
                    if any(ma_bo_phan_sua in l for l in data_bo_phan.keys()) == True:
                        new_dict_nhan_vien["Mã bộ phận"] = ma_bo_phan_sua
                        break
                    else:
                        print("Mã bộ phận không tồn tại, vui lòng nhập lại!")
                        continue
    
            # Chỉnh sửa chức vụ:
            while True:
                # Nếu chức vụ không đổi, giữ nguyên giá trị từ data_nhan_vien:
                chuc_vu_sua = input("Nhập chức vụ (Quản lý / Nhân viên): ")    
                if chuc_vu_sua == "":
                    new_dict_nhan_vien["Chức vụ"] = data_nhan_vien[k]["Chức vụ"]
                    break
                # Nếu chức vụ thay đổi, sử dụng giá trị mới của chức vụ được nhập vào, lưu ý, chỉ được nhập vào "Quản lý" hoặc "Nhân viên":
                else:
                    if (chuc_vu_sua == "Quản lý") or (chuc_vu_sua == "Nhân viên"):
                        new_dict_nhan_vien["Chức vụ"] = chuc_vu_sua
                        break
                    else:
                        print('Xin nhập "Quản lý" hoặc nhập "Nhân viên"!')   
                        continue     

            # Chỉnh sửa họ và tên:
            while True:
                ho_va_ten_sua = input("Nhập họ và tên: ")
                # Nếu họ và tên không đổi, giữ nguyên giá trị từ data_nhan_vien:
                if ho_va_ten_sua == "":
                    new_dict_nhan_vien["Họ và tên"] = data_nhan_vien[k]["Họ và tên"]
                    break
                # Nếu họ và tên thay đổi, sử dụng giá trị mới của họ và tên được nhập vào:
                else:
                    new_dict_nhan_vien["Họ và tên"] = ho_va_ten_sua
                    break
            
            # Chỉnh sửa hệ số lương: 
            while True:
                he_so_luong_sua = input("Nhập hệ số lương: ")
                # Nếu hệ số lương không đổi, giữ nguyên giá trị từ data_nhan_vien:
                try:
                    if int(he_so_luong_sua) > 0:
                        new_dict_nhan_vien["Hệ số lương"] = int(he_so_luong_sua)
                        break 
                    elif int(he_so_luong_sua) < 0:
                        print("Bạn cần nhập đúng định dạng!")
                        continue
                except:
                    new_dict_nhan_vien["Hệ số lương"] = data_nhan_vien[k]["Hệ số lương"]
                    break

            # Chỉnh sửa số ngày làm việc:
            while True:
                so_ngay_lam_viec_sua = input("Nhập số ngày làm việc: ")
                try:
                    if int(so_ngay_lam_viec_sua) > 0:
                        new_dict_nhan_vien["Số ngày làm việc"] = int(so_ngay_lam_viec_sua)
                        break
                    elif int(so_ngay_lam_viec_sua) < 0:
                        print("Bạn cần nhập đúng định dạng!")
                        continue
                except:
                    new_dict_nhan_vien["Số ngày làm việc"] = data_nhan_vien[k]["Số ngày làm việc"]
                    break
            
            # Chỉnh sửa hệ số hiệu quả:
            while True:
                he_so_hieu_qua_sua = input("Nhập hệ số hiệu quả: ")
                try:
                    if float(he_so_hieu_qua_sua) >= 0:
                        new_dict_nhan_vien["Hệ số hiệu quả"] = float(he_so_hieu_qua_sua)
                        break
                    elif float(he_so_hieu_qua_sua) < 0:
                        print("Bạn cần nhập đúng định dạng!")
                        continue
                except:
                    new_dict_nhan_vien["Hệ số hiệu quả"] = data_nhan_vien[k]["Hệ số hiệu quả"]
                    break

            # Chỉnh sửa thưởng nhân viên:
            while True:
                thuong_sua = input("Nhập thưởng: ")
                try:
                    if int(thuong_sua) >= 0:
                        new_dict_nhan_vien["Thưởng"] = int(thuong_sua)
                        break
                    elif int(thuong_sua) < 0:
                        print("Bạn cần nhập đúng định dạng!")
                        continue
                except:
                    new_dict_nhan_vien["Thưởng"] = data_nhan_vien[k]["Thưởng"]
                    break

            # Chỉnh sửa số ngày đi muộn:
            while True:
                so_ngay_di_muon_sua = input("Nhập số ngày đi muộn: ")
                try:
                    if int(so_ngay_di_muon_sua) >= 0:
                        new_dict_nhan_vien["Số ngày đi muộn"] = int(so_ngay_di_muon_sua)
                        break
                    elif int(so_ngay_di_muon_sua) < 0:
                        print("Bạn cần nhập đúng định dạng!")
                        continue
                except:
                    new_dict_nhan_vien["Số ngày đi muộn"] = data_nhan_vien[k]["Số ngày đi muộn"]
                    break
    
    # Ghi dữ liệu sửa vào file "nhan_vien.json":
    for n in data_nhan_vien:
        if ma_nhan_vien_can_sua == n["Mã số"]:
            n.update(new_dict_nhan_vien)
    print("\nĐã hoàn tất chỉnh sửa")
    print("-----")
    f_bo_phan = open("nhan_vien.json","w", encoding = "utf-8")
    json.dump(data_nhan_vien, f_bo_phan, ensure_ascii = False, indent = 4)
    f_bo_phan.close()

    # In dữ liệu sửa:
    print("Thông tin mới của nhân viên")
    print("Mã số: {}".format(new_dict_nhan_vien["Mã số"]))
    print("Mã bộ phận: {}".format(new_dict_nhan_vien["Mã bộ phận"]))
    print("Chức vụ: {}".format(new_dict_nhan_vien["Chức vụ"]))
    print("Họ và tên: {}".format(new_dict_nhan_vien["Họ và tên"]))
    print("Hệ số lương: {:,}".format(new_dict_nhan_vien["Hệ số lương"]))
    print("Số ngày làm việc: {}".format(new_dict_nhan_vien["Số ngày làm việc"]))
    print("Hệ số hiệu quả: {}".format(new_dict_nhan_vien["Hệ số hiệu quả"]))
    print("Thưởng: {:,}".format(new_dict_nhan_vien["Thưởng"]))
    print("Số ngày đi muộn: {}".format(new_dict_nhan_vien["Số ngày đi muộn"]))

# Hàm tính lương thực nhận:
def tinh_luong(data_json_late_coming, data_xml_tax_calculating, data_nhan_vien, data_bo_phan):

    # Chạy vòng lặp qua data_nhan_vien (Là 1 list lớn chứa các dictionary nhỏ tượng trưng cho từng nhân viên):
    for dict_nhan_vien in data_nhan_vien:
        Nhan_Vien = Employee(dict_nhan_vien["Mã số"], dict_nhan_vien["Họ và tên"], dict_nhan_vien["Hệ số lương"], dict_nhan_vien["Số ngày làm việc"], dict_nhan_vien["Mã bộ phận"], dict_nhan_vien["Hệ số hiệu quả"], dict_nhan_vien["Thưởng"], dict_nhan_vien["Số ngày đi muộn"])
        Quan_Ly = Manager(dict_nhan_vien["Mã số"], dict_nhan_vien["Họ và tên"], dict_nhan_vien["Hệ số lương"], dict_nhan_vien["Số ngày làm việc"], dict_nhan_vien["Mã bộ phận"], dict_nhan_vien["Hệ số hiệu quả"], dict_nhan_vien["Thưởng"], dict_nhan_vien["Số ngày đi muộn"])
        Bo_Phan = Department(dict_nhan_vien["Mã bộ phận"], data_bo_phan[dict_nhan_vien["Mã bộ phận"]])
        # Tính tổng thu nhập chưa thuế = tổng thu nhập chưa thưởng + thưởng (bonus) + thưởng bộ phận - tiền phạt đi muộn.
        # Tính lương thực nhận = tổng thu nhập chưa thuế - thuế TNCN cần nộp.
        # Lương của nhân viên và quản lý sẽ được tính khác nhau, nếu là quản lý sẽ nhận thêm 10% thưởng bộ phận, còn nhân viên thì không.
        # Dữ liệu tính tiền phạt đi muộn và tính thuế TNCN được lấy từ các list tại hàm main(), các dữ liệu này được trích xuất từ 2 đường link json và xml.
        # Thực hiện so sánh số ngày đi muộn để lấy ra tiền phạt đi muộn cho một ngày tương ứng.
        # Thực hiện so sánh tổng thu nhập chưa thuế để lấy ra phần trăm nộp thuế và tính lương thực nhận.
        for i in range(len(data_json_late_coming) - 1): # Chạy vòng lặp qua 3 dictionary.
            min_late_coming = data_json_late_coming[i]["min"] # Giá trị min_late_coming (0, 3 và 6).
            max_late_coming = data_json_late_coming[i]["max"] # Giá trị max_late_coming (3 và 6).
            amount_late_coming = data_json_late_coming[i]["value"] # Giá trị phạt đi muộn (20000, 30000 và 50000).
            if Nhan_Vien.so_ngay_di_muon > min_late_coming and Nhan_Vien.so_ngay_di_muon <= max_late_coming: # (0<x<=3 và 3<x<=6).
                if dict_nhan_vien["Chức vụ"] == "Nhân viên":
                    tong_thu_nhap_chua_thue = (Nhan_Vien.tong_thu_nhap_chua_thuong + Nhan_Vien.thuong + Bo_Phan.get_bonus_salary() - amount_late_coming * Nhan_Vien.so_ngay_di_muon) * 0.895
                else:
                    tong_thu_nhap_chua_thue = (Quan_Ly.tong_thu_nhap_chua_thuong + Quan_Ly.thuong + 1.1 * Bo_Phan.get_bonus_salary() - amount_late_coming * Quan_Ly.so_ngay_di_muon) * 0.895
            elif Nhan_Vien.so_ngay_di_muon > data_json_late_coming[len(data_json_late_coming) - 1]["min"]: # Lấy đúng giá trị 6.
                if dict_nhan_vien["Chức vụ"] == "Nhân viên":
                    tong_thu_nhap_chua_thue = (Nhan_Vien.tong_thu_nhap_chua_thuong + Nhan_Vien.thuong + Bo_Phan.get_bonus_salary() - data_json_late_coming[len(data_json_late_coming) - 1]["value"] * Nhan_Vien.so_ngay_di_muon) * 0.895
                else:
                    tong_thu_nhap_chua_thue = (Quan_Ly.tong_thu_nhap_chua_thuong + Quan_Ly.thuong + 1.1 * Bo_Phan.get_bonus_salary() - data_json_late_coming[len(data_json_late_coming) - 1]["value"] * Quan_Ly.so_ngay_di_muon) * 0.895
        for j in range(len(data_xml_tax_calculating) - 1): 
            min_salary_to_pay_tax = int(data_xml_tax_calculating[j]["min"]) * pow(10,6)
            max_salary_to_pay_tax = int(data_xml_tax_calculating[j]["max"]) * pow(10,6)
            percent_tax_to_pay = int(data_xml_tax_calculating[j]["value"]) / 100
            if int(tong_thu_nhap_chua_thue) > min_salary_to_pay_tax and int(tong_thu_nhap_chua_thue) <= max_salary_to_pay_tax:
                luong_thuc_nhan = tong_thu_nhap_chua_thue - tong_thu_nhap_chua_thue * percent_tax_to_pay
            elif int(tong_thu_nhap_chua_thue) > (int(data_xml_tax_calculating[len(data_xml_tax_calculating) - 1]["min"])) * pow(10,6):
                luong_thuc_nhan = tong_thu_nhap_chua_thue - tong_thu_nhap_chua_thue * int(data_xml_tax_calculating[len(data_xml_tax_calculating) - 1]["value"]) / 100
        
        # In bảng lương theo đúng format từ yêu cầu đề bài:
        print("-----")
        print("Mã số: {}".format(dict_nhan_vien["Mã số"]))
        print("Thu nhập thực nhận: {:,} (VNĐ)".format(int(luong_thuc_nhan)))
        print("-----\n")

# Hàm main() dùng để thực thi chương trình:
if __name__ == "__main__":

    # Bỏ qua lỗi chứng chỉ ssl:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Trích xuất dữ liệu từ đường dẫn json:
    url_json = "https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de"
    url_json_read = urllib.request.urlopen(url_json, context = ctx).read()
    data_json_late_coming = json.loads(url_json_read)

    # Trích xuất dữ liệu từ đường dẫn xml:
    url_xml = "https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7"
    url_xml_read = urllib.request.urlopen(url_xml, context = ctx).read()
    tree = ET.fromstring(url_xml_read)
    data_xml_tax_calculating = list()
    for child_tag in tree:
        tax_dict = dict()
        for tax_info in child_tag:
            if tax_info.tag == "min":
                tax_dict["min"] = tax_info.text
            elif tax_info.tag == "max":
                tax_dict["max"] = tax_info.text
            else:
                tax_dict["value"] = tax_info.text
        data_xml_tax_calculating.append(tax_dict)
    data_xml_tax_calculating.pop(3) # Xoá dict ở vị trí thứ 4 (Index = 3) vì trùng với dict đầu tiên.

    # Đọc file "nhan_vien.json" để lấy dữ liệu nhân viên nhằm mục đích tính lương:
    f_nhan_vien = open("nhan_vien.json","r", encoding = "utf-8")
    data_nhan_vien = json.loads(f_nhan_vien.read())
    f_nhan_vien.close()

    # Đọc file "bo_phan.json" để lấy dữ liệu thưởng bộ phận:
    f_bo_phan = open("bo_phan.json","r", encoding = "utf-8")
    data_bo_phan = json.loads(f_bo_phan.read())
    f_bo_phan.close()

    # Menu chức năng:
    while True:
        print("""
        1. Hiển thị danh sách nhân viên.
        2. Hiển thị danh sách bộ phận.
        3. Thêm nhân viên mới.
        4. Xoá nhân viên theo ID.
        5. Xoá bộ phận theo ID.
        6. Chỉnh sửa nhân viên.
        7. Hiển thị bảng lương.
        8. Thoát.
        """)
        select = input("Mời bạn nhập chức năng mong muốn: ")
        if str(select).isdigit():
            select = int(select)
            if select == 1:
                hien_thi_nhan_vien(data_nhan_vien)
            elif select == 2:
                hien_thi_bo_phan(data_bo_phan)
            elif select == 3:
                them_nhan_vien_moi(data_nhan_vien, data_bo_phan)
            elif select == 4:
                xoa_nhan_vien_theo_ID(data_nhan_vien)
            elif select == 5:
                xoa_bo_phan_theo_ID(data_nhan_vien, data_bo_phan)
            elif select == 6:
                sua_nhan_vien(data_nhan_vien, data_bo_phan)
            elif select == 7:
                tinh_luong(data_json_late_coming, data_xml_tax_calculating, data_nhan_vien, data_bo_phan)
            elif select == 8:
                sys.exit()
            else:
                print("Chức năng không tồn tại, vui lòng chọn lại chức năng mong muốn.")
        else:
            print("Thông tin nhập vào không hợp lệ, vui lòng nhập lại!")
