import math

# Nhập toạ độ các điểm A,B,C (Input đầu vào cho tất cả các hàm theo yêu cầu đề bài):
while True:
    try:
        xA = input("Nhập hoành độ điểm A: ")
        if (xA.isalpha()):
            print(">>> Nhập lại hoành độ điểm A")
        else:
            xA = float(xA)
        break
    except:
        print(">>> Nhập lại hoành độ điểm A")
while True:  
    try:  
        yA = input("Nhập tung độ điểm A: ")
        if (yA.isalpha()):
            print(">>> Nhập lại tung độ điểm A")
        else: 
            yA = float(yA)
            break
    except:
        print(">>> Nhập lại tung độ điểm A")
while True:
    try:    
        xB = input("Nhập hoành độ điểm B: ")
        if (xB.isalpha()):
            print(">>> Nhập lại hoành độ điểm B")
        else: 
            xB = float(xB)
            break
    except:
        print(">>> Nhập lại hoành độ điểm B")
while True:
    try:   
        yB = input("Nhập tung độ điểm B: ")
        if (yB.isalpha()):
            print(">>> Nhập lại tung độ điểm B")
        else: 
            yB = float(yB)
            break
    except:
        print(">>> Nhập lại tung độ điểm B")
while True:    
    try:
        xC = input("Nhập hoành độ điểm C: ")
        if (xC.isalpha()):
            print(">>> Nhập lại hoành độ điểm C")
        else: 
            xC = float(xC)
            break
    except:
        print("Nhập lại hoành độ điểm C")
while True:
    try:
        yC = input("Nhập tung độ điểm C: ")
        if (yC.isalpha()):
            print(">>> Nhập lại tung độ điểm C")
        else: 
            yC = float(yC)
            break
    except:
        print("Nhập lại tung độ điểm C")

# Hàm kiểm tra 3 điểm A,B,C có tạo thành tam giác không:
def kiemtra_tamgiac(xA,xB,xC,yA,yB,yC):
    try:    
        x_vector_AB = xB - xA
        y_vector_AB = yB - yA
        x_vector_BC = xC - xB
        y_vector_BC = yC - yB
        if (x_vector_AB / x_vector_BC) != (y_vector_AB / y_vector_BC):
            return True
        else:
            return False
    except:
        return False

# Hàm tính độ dài các cạnh và các góc của tam giác:
def goccanh_tamgiac(xA,xB,xC,yA,yB,yC):
    AB = round(math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)),2)
    BC = round(math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)),2)
    AC = round(math.sqrt(pow(xC-xA,2) + pow(yC-yA,2)),2)
    goc_A = round((math.degrees(math.acos((AB**2 + AC**2 - BC**2) / (2 * AB * AC)))),2)
    goc_B = round((math.degrees(math.acos((AB**2 + BC**2 - AC**2) / (2 * AB * BC)))),2)
    goc_C = round((math.degrees(math.acos((AC**2 + BC**2 - AB**2) / (2 * AC * BC)))),2)
    goc_canh_tamgiac = [AB,BC,AC,goc_A,goc_B,goc_C]
    return goc_canh_tamgiac

# Hàm xét tam giác ABC là loại tam giác nào (Theo thứ tự đề bài: Vuông cân, đều, tù và cân, vuông hoặc cân hoặc tù, thường):
def xet_tamgiac(xA,xB,xC,yA,yB,yC):
    a = round((math.degrees(math.acos((round(math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)),2)**2 + round(math.sqrt(pow(xC-xA,2) + pow(yC-yA,2)),2)**2 - round(math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)),2)**2) / (2 * round(math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)),2) * round(math.sqrt(pow(xC-xA,2) + pow(yC-yA,2)),2))))),2)
    b = round((math.degrees(math.acos((round(math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)),2)**2 + round(math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)),2)**2 - round(math.sqrt(pow(xC-xA,2) + pow(yC-yA,2)),2)**2) / (2 * round(math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)),2) * round(math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)),2))))),2)
    c = round((math.degrees(math.acos((round(math.sqrt(pow(xC-xA,2) + pow(yC-yA,2)),2)**2 + round(math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)),2)**2 - round(math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)),2)**2) / (2 * round(math.sqrt(pow(xC-xA,2) + pow(yC-yA,2)),2) * round(math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)),2))))),2)
    check_tamgiac = None
    if (a == 90) and (b == c):
        check_tamgiac = "Tam giác ABC là tam giác vuông cân tại A"
    elif (b == 90) and (a == c):
        check_tamgiac = "Tam giác ABC là tam giác vuông cân tại B"
    elif (c == 90) and (a == b):
        check_tamgiac = "Tam giác ABC là tam giác vuông cân tại C"
    elif (a == b) and (b == c):
        check_tamgiac = "Tam giác ABC là tam giác đều"
    elif (a > 90) and (b == c):
        check_tamgiac = "Tam giác ABC là tam giác tù và cân tại A"
    elif (b > 90) and (a == c):
        check_tamgiac = "Tam giác ABC là tam giác tù và cân tại B"
    elif (c > 90) and (a == b):
        check_tamgiac = "Tam giác ABC là tam giác tù và cân tại C"
    elif (a == 90) and (b != c):
        check_tamgiac = "Tam giác ABC là tam giác vuông tại A"
    elif (b == 90) and (a != c):
        check_tamgiac = "Tam giác ABC là tam giác vuông tại B"
    elif (c == 90) and (a != b):
        check_tamgiac = "Tam giác ABC là tam giác vuông tại C"
    elif (b == c) and (b != a):
        check_tamgiac = "Tam giác ABC là tam giác cân tại A"
    elif (a == c) and (a != b):
        check_tamgiac = "Tam giác ABC là tam giác cân tại B"
    elif (a == b) and (a != c):
        check_tamgiac = "Tam giác ABC là tam giác cân tại C"
    elif (a > 90) and (b != c):
        check_tamgiac = "Tam giác ABC là tam giác tù tại đỉnh A"
    elif (b > 90) and (a != c):
        check_tamgiac = "Tam giác ABC là tam giác tù tại đỉnh B"
    elif (c > 90) and (a != b):
        check_tamgiac = "Tam giác ABC là tam giác tù tại đỉnh C"
    else:
        check_tamgiac = "Tam giác ABC là tam giác thường"
    return check_tamgiac

# Hàm tính diện tích tam giác:
def dientich_tamgiac(xA,xB,xC,yA,yB,yC):
    S_ABC = round(1/2 * round(math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)) * 
    (math.sin(math.radians(round((math.degrees(math.acos((math.sqrt(pow(xB-xA,2) + pow(yB-yA,2))**2 + math.sqrt(pow(xC-xB,2) + pow(yC-yB,2))**2 - math.sqrt(pow(xC-xA,2) + pow(yC-yA,2))**2) / 
    (2 * math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)) * math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)))))),2)))),2) * round(math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)),2),2)
    return S_ABC
    
# Hàm tính độ dài các đường cao (AH, BI, CK) trong tam giác ABC:
def duongcao_tamgiac(xA,xB,xC,yA,yB,yC):
    AH = round(math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)) * (math.sin(math.radians(round((math.degrees(math.acos((math.sqrt(pow(xB-xA,2) + pow(yB-yA,2))**2 + math.sqrt(pow(xC-xB,2) + pow(yC-yB,2))**2 - math.sqrt(pow(xC-xA,2) + pow(yC-yA,2))**2) / (2 * math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)) * math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)))))),2)))),2)
    BI = round(math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)) * (math.sin(math.radians(round((math.degrees(math.acos((math.sqrt(pow(xB-xA,2) + pow(yB-yA,2))**2 + math.sqrt(pow(xC-xA,2) + pow(yC-yA,2))**2 - math.sqrt(pow(xC-xB,2) + pow(yC-yB,2))**2) / (2 * math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)) * math.sqrt(pow(xC-xA,2) + pow(yC-yA,2)))))),2)))),2)
    CK = round(math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)) * (math.sin(math.radians(round((math.degrees(math.acos((math.sqrt(pow(xB-xA,2) + pow(yB-yA,2))**2 + math.sqrt(pow(xC-xB,2) + pow(yC-yB,2))**2 - math.sqrt(pow(xC-xA,2) + pow(yC-yA,2))**2) / (2 * math.sqrt(pow(xB-xA,2) + pow(yB-yA,2)) * math.sqrt(pow(xC-xB,2) + pow(yC-yB,2)))))),2)))),2)
    # Độ dài các đường cao AH,BI,CK của tam giác ABC được lưu thành một list:
    duongcao = [AH,BI,CK]
    return duongcao

# Hàm giaima_tamgiac():
def giaima_tamgiac(xA,xB,xC,yA,yB,yC):
    if kiemtra_tamgiac(xA,xB,xC,yA,yB,yC) is False:
        print("3 điểm A,B,C không hợp thành một tam giác")
    else:
        print("3 điểm A,B,C hợp thành một tam giác")
        print("1. Số đo cơ bản của tam giác: ")
        print("- Chiều dài cạnh AB: " + str(goccanh_tamgiac(xA,xB,xC,yA,yB,yC)[0]))
        print("- Chiều dài cạnh BC: " + str(goccanh_tamgiac(xA,xB,xC,yA,yB,yC)[1]))
        print("- Chiều dài cạnh AC: " + str(goccanh_tamgiac(xA,xB,xC,yA,yB,yC)[2]))
        print("- Độ lớn góc A: " + str(goccanh_tamgiac(xA,xB,xC,yA,yB,yC)[3]) + " độ")
        print("- Độ lớn góc B: " + str(goccanh_tamgiac(xA,xB,xC,yA,yB,yC)[4]) + " độ")
        print("- Độ lớn góc C: " + str(goccanh_tamgiac(xA,xB,xC,yA,yB,yC)[5]) + " độ")
        print(xet_tamgiac(xA,xB,xC,yA,yB,yC))
        print("2. Diện tích của tam giác ABC: " + str(dientich_tamgiac(xA,xB,xC,yA,yB,yC)))
        print("3. Số đo nâng cao của tam giác: ")
        print("- Độ dài đường cao từ đỉnh A = AH: " + str(duongcao_tamgiac(xA,xB,xC,yA,yB,yC)[0]))
        print("- Độ dài đường cao từ đỉnh B = BI: " + str(duongcao_tamgiac(xA,xB,xC,yA,yB,yC)[1]))
        print("- Độ dài đường cao từ đỉnh C = CK: " + str(duongcao_tamgiac(xA,xB,xC,yA,yB,yC)[2]))
        print("- Khoảng cách từ đỉnh A đến trọng tâm của tam giác: " + str((round(2/3 * trungtuyen_tamgiac(xA,xB,xC,yA,yB,yC)[0],2))))
        print("- Khoảng cách từ đỉnh B đến trọng tâm của tam giác: " + str((round(2/3 * trungtuyen_tamgiac(xA,xB,xC,yA,yB,yC)[1],2))))
        print("- Khoảng cách từ đỉnh C đến trọng tâm của tam giác: " + str((round(2/3 * trungtuyen_tamgiac(xA,xB,xC,yA,yB,yC)[2],2))))
        print("4. Toạ độ một số điểm đặc biệt của tam giác: ")
        print("- Toạ độ trọng tâm: " + str([tam_tamgiac(xA,xB,xC,yA,yB,yC)[0],tam_tamgiac(xA,xB,xC,yA,yB,yC)[1]]))
        print("- Toạ độ trực tâm: " + str([tam_tamgiac(xA,xB,xC,yA,yB,yC)[2],tam_tamgiac(xA,xB,xC,yA,yB,yC)[3]]))
        return kiemtra_tamgiac(xA,xB,xC,yA,yB,yC), goccanh_tamgiac(xA,xB,xC,yA,yB,yC), xet_tamgiac(xA,xB,xC,yA,yB,yC), dientich_tamgiac(xA,xB,xC,yA,yB,yC)

# Hàm tính độ dài các đường trung tuyến của tam giác ABC:
def trungtuyen_tamgiac(xA,xB,xC,yA,yB,yC):
    # Trung điểm M,N,P của các cạnh AB,BC,AC của tam giác ABC:
    xM = (xA + xB) / 2
    yM = (yA + yB) / 2
    xN = (xB + xC) / 2
    yN = (yB + yC) / 2
    xP = (xA + xC) / 2
    yP = (yA + yC) / 2
    # Các đường trung tuyến AN, BP, CM:
    AN = round((math.sqrt(pow(xN-xA,2) + pow(yN-yA,2))),2)
    BP = round((math.sqrt(pow(xP-xB,2) + pow(yP-yB,2))),2)
    CM = round((math.sqrt(pow(xM-xC,2) + pow(yM-yC,2))),2)
    trungtuyen = [AN,BP,CM]
    return trungtuyen

# Hàm tính toạ độ trọng tâm (G) và trực tâm (T) của tam giác ABC:
def tam_tamgiac(xA,xB,xC,yA,yB,yC):
    xG = round(((xA + xB + xC) / 3),2)
    yG = round(((yA + yB + yC) / 3),2)
    yT = round((((xB-xA)+(yA*((yC-yB)/(xC-xB)))-(yB*((yC-yA)/(xC-xA)))) / (((yC-yB)/(xC-xB))-((yC-yA)/(xC-xA)))),2)
    xT = round((((-(yT-yA)*(yC-yB))/(xC-xB)) + xA),2)
    trongtam_tructam = [xG,yG,xT,yT]
    return trongtam_tructam

giaima_tamgiac(xA,xB,xC,yA,yB,yC)