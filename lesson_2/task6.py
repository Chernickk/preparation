class ItemDiscount:
    __name = 'name'
    price = 1200

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.price

    def set_name(self, name):
        ItemDiscount.__name = name

    def set_price(self, price):
        ItemDiscount.price = price


class ItemDiscountReport1(ItemDiscount):

    def get_info(self):
        return super().get_name()


class ItemDiscountReport2(ItemDiscount):

    def get_info(self):
        return super().get_price()


idr1 = ItemDiscountReport1()
idr2 = ItemDiscountReport2()

for _class in idr1, idr2:
    print(_class.get_info())
