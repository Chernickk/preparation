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


class ItemDiscountReport(ItemDiscount):
    def __init__(self, discount):
        self.discount = discount

    def __str__(self):
        return f'{super().get_name()}: {super().get_price() * ((100 - self.discount) / 100)}'

    def get_parent_data(self):
        return f'{super().get_name()}: {super().get_price()}'


parent = ItemDiscount()
child = ItemDiscountReport(20)  # percents

print(child)
