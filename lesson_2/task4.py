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
    def get_parent_data(self):
        return f'{super().get_name()}: {super().get_price()}'


parent = ItemDiscount()
child = ItemDiscountReport()

print(child.get_parent_data())

parent.set_price(999)
parent.set_name('parent_name')
print(parent.get_name(), parent.get_price())
print(child.get_parent_data())
