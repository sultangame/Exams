class Shop:
    def __init__(self, name,  sum, colic):
        self.name = name
        self.sum = sum
        self.colic = colic
    def description(self):
         return f"{self.name} это хороший бюджетный смартфон "
    def Smart(self):
        if self.colic < b:
            return f"У нас не достаточно товара"
    def bought(self):
        return self.sum * b
b = int(input("Введите количество телефонов:"))
smartphone = Shop("Redmi", 5000, 45)
print(smartphone.bought())
print(smartphone.Smart())
print(smartphone.description())
