class ItemDiscount:
    __name = 'name'
    __price = 1200

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{super().get_name()}: {super().get_price()}'


idr = ItemDiscountReport()
try:
    result = idr.get_parent_data()
    print(result)
except AttributeError:
    print("It's a private attrs!")
