string_input = input("Nhập chuỗi: ").split()
def get_three_letter_words(string_input):
    return [i for i in string_input if len(i) > 3]
print(get_three_letter_words(string_input))