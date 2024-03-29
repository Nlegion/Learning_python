# Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.name

    @property
    def get_price(self):
        return self.price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print("товар: ", self._get_name, " цена: ", self._get_price)


item = ItemDiscountReport("Epson", 3)
item.get_parent_data()
