class AppleBasket:
    def __init__(self, apple_colour, apple_quantity):
        self.mau_qua_tao = apple_colour
        self.so_luong_tao = apple_quantity
    def increase(self):
        self.so_luong_tao = self.so_luong_tao + 1
        return self.so_luong_tao

test_one = AppleBasket("Red", 4)
print("A basket of {0} {1} apples.".format(test_one.so_luong_tao, test_one.mau_qua_tao))
test_one.increase()
print("A basket of {0} {1} apples.".format(test_one.so_luong_tao, test_one.mau_qua_tao))