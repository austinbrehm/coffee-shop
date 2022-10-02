from tkinter import *
from tkinter import ttk


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

    def gui():
        root = Tk()
        root.title("Fuego Coffee Shop")
        root.iconbitmap('coffeemug.ico')
        root.geometry('400x400')
        # the root window is the main window of the application, an instance of the Tk class. The window is a 3x3 grid
        frm = ttk.Frame(root, padding=20)
        # frame widgets fit inside the root window and contains a label and button
        frm.grid()
        # grid places the form inside the window
        menu = ttk.Label(frm, text='Menu', font=('Arial', 18, 'bold')).grid(row=0, column=0)
        drip = ttk.Label(frm, text='Drip Brew: ', font=('Arial', 12)).grid(row=1, column=0)
        latte = ttk.Label(frm, text='Latte: ', font=('Arial', 12)).grid(row=2, column=0)
        cappuccino = ttk.Label(frm, text='Cappuccino: ', font=('Arial', 12)).grid(row=3, column=0)
        ttk.Button(frm, text="Order").grid(row=4, column=0)
        ttk.Button(frm, text="Exit", command=root.destroy).grid(row=4, column=1)
        root.mainloop()
        # mainloop method shows the window and terminates with user input

    gui()

    # while True:
    # menu()
    # option = int(input('Select an option: '))
    # if option == 1:
    #     pass
    # if option == 2:
    #     print('Thank you for visiting the coffee shop. Good bye!')
    #     break


if __name__ == '__main__':
    main()
