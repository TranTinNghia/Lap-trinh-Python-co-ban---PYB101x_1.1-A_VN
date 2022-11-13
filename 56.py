res = [input("Nhập số: ") for i in range(int(input("Nhập số giá trị trong list: ")))]
string_result = str()
for j in res:
    string_result = string_result + str(j)
print(string_result)