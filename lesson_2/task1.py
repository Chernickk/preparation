class ItemDiscount:
    name = 'name'
    price = 1200


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{super().name}: {super().price}'


idr = ItemDiscountReport()
result = idr.get_parent_data()
print(result)
