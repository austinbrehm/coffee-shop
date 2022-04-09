class Coffee:
    def __init__(self, size):
        self.size = size

    def print_size(self):
        print(f"Size: {self.size}")


class Latte(Coffee):
    def __init__(self, size, espresso, milk, flavor):
        super().__init__(size)
        self.espresso = espresso
        self.milk = milk
        self.flavor = flavor


class Cappuccino(Coffee):
    def __init__(self, size, espresso, milk, flavor):
        super().__init__(size)
        self.espresso = espresso
        self.milk = milk
        self.flavor = flavor


class DripBrew(Coffee):
    def __init__(self, size, roast, creamer, sugar):
        super().__init__(size)
        self.roast = roast
        self.creamer = creamer
        self.sugar = sugar


new_order = Latte('small', 'regula', '2%', 'none')
new_order.print_size()
