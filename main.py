def main():
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

    def menu():
        print("\nMain Menu\n"
              "1. Order\n"
              "2. Exit"
              )
    print('\nWelcome to the coffee shop!')
    new_order = Latte('small', 'regular', '2%', 'none')

    while True:
        menu()
        option = int(input('Select an option: '))
        if option == 1:
            pass
        if option == 2:
            print('Thank you for visiting the coffee shop. Good bye!')
            break


if __name__ == '__main__':
    main()
