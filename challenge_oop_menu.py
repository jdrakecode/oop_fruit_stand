from challenge_oop import Fruit, Barrel

class Menu:
    def __init__(self):
        self.barrel = Barrel()
        self.choice = {
            "1": self.add_to,
            "2": self.get_type,
            "3": self.remove_from,
            "4": self.reset_barrel,
            "5": exit
        }

    def display_menu(self):
        print(
"""
Menu:
1. Add to barrel
2. Get fruit type
3. Remove from barrel
4. Empty barrel
5. Exit
"""
        )
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def add_to(self):
        Fruit.name = input("What fruit do you want to add?\n> ")
        # Fruit.price = ???
        self.barrel.add_fruit(Fruit.name)
        print(f"There are now {self.barrel.fruit_count} {Fruit.name}s in the barrel")

    def get_type(self):
        print(f"The barrel conftains {self.barrel.fruit_count} {Fruit.name}s")

    def remove_from(self):
        Fruit.name = input("What fruit do you want to remove?\n> ")
        self.barrel.sub_fruit(Fruit.name)
        print(f"There are now {self.barrel.fruit_count} {Fruit.name}s in the barrel")

    def reset_barrel(self):
        Fruit.name = input("What fruit barrel do you want to empty?\n> ")
        self.barrel.empty(Fruit.name)
        print(f"There are now {self.barrel.fruit_count} {Fruit.name}s in the barrel")

if __name__ == "__main__":
    menu = Menu()
    menu.run()
