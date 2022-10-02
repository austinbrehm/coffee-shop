from tkinter import *
from tkinter import ttk
root = Tk()
# the root window is the main window of the application, an instance of the Tk class. The window is a 3x3 grid
frm = ttk.Frame(root, padding=20)
# frame widgets fit inside the root window and contains a label and button
def print_hello():
    print('hello')

frm.grid()
# grid places the form inside the window
ttk.Label(frm, text="Main Menu").grid(column=0, row=0)
ttk.Button(frm, text="Order").grid(column=1, row=1)
ttk.Button(frm, text="Exit", command=root.destroy).grid(column=2, row=1)
root.mainloop()
# mainloop method shows the window and terminates with user input


def main():

    class Coffee:
        def __init__(self, size):
            self.size = size

        def get_size(self):
            return self.size

        def set_size(self):
            pass

    class Latte(Coffee):
        price = 3.00

        def __init__(self, size, espresso, milk, flavor):
            super().__init__(size)
            self.espresso = espresso
            self.milk = milk
            self.flavor = flavor

        def get_espresso(self):
            return self.espresso

        def set_espresso(self):
            options = [1, 2, 3]
            shots = input("Enter the amount of espresso shots: ")
            if shots in options:
                self.espresso = shots
            else:
                pass

        def get_milk(self):
            return self.milk

        def set_milk(self):
            pass

        def get_flavor(self):
            return self.flavor

        def set_flavor(self):
            pass

    class Cappuccino(Coffee):
        price = 3.00

        def __init__(self, size, espresso, milk, flavor):
            super().__init__(size)
            self.espresso = espresso
            self.milk = milk
            self.flavor = flavor

    class DripBrew(Coffee):
        price = 3.00

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
    new_order = Latte('small', 2, '2%', 'none')

    while True:
        menu()
        option = int(input('Select an option: '))
        if option == 1:
            pass
        if option == 2:
            print('Thank you for visiting the coffee shop. Good bye!')
            break


# if __name__ == '__main__':
    # main()