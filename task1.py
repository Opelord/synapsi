from random import randint
import data


class Product(data.ParentProduct):
    def __init__(self, name, amount, price):
        super().__init__(name)
        self.amount = amount
        self.price = price

    def show_price(self, currency):
        print(f"{self.name} price is {self.price}")

    def show_amount(self):
        print(f"{self.name} price is {self.amount}")

    def calculate_total_value(self):
        return self.amount*self.price

    def __str__(self):
        return f"Name: {self.name}, amount: {self.amount}, price: {self.price}"


for p in data.products:
    p["amount"] = randint(p["amount"]["min"], p["amount"]["max"])
    p["price"] = randint(p["price"]["min"], p["price"]["max"])


for p in data.products:
    data.obj_list.append(Product(p["name"], p["amount"], p["price"]))


summary = []
for o in data.obj_list:
    summary.append(o.calculate_total_value())

with open("results_01.txt", "w") as f:
    for i in range(len(summary)):
        f.write(f"Summary: {summary[i]}, Product: {data.products[i]}, Object: {data.obj_list[i]}\n")

