class ItemDiscount:
    __name = 'name'
    __price = 1200


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{super().__name}: {super().__price}'


idr = ItemDiscountReport()
try:
    result = idr.get_parent_data()
except AttributeError:
    print("It's a private attrs!")
