from classes.home_kitchen import HomeKitchen
from classes.pizzeria import Pizzeria
from classes.pub import Pub
from classes.restaurant import Restaurant


class KitchenManager:
    """
    Class creates an array of objects and helps to call main function
    :param kitchens - an array of abstract class`s children objects
    """
    kitchens = []

    def add_kitchen(self, kitchen):
        """
        Method which adds kitchens to array
        :param kitchen: name of objects in general
        :return: an addition of kitchen to array
        """
        self.kitchens.append(kitchen)

    def find_bigger_than(self, size):
        """
        Method finds all objects bigger than given size
        :param size: of place
        :return: a filtered list with needed objects
        """
        return list(filter(lambda kitchen: kitchen.size > size, self.kitchens))

    def find_bigger_capacity_than(self, capacity):
        """
        Method finds all objects with bigger capacity than given size
        :param capacity: of possible people in place
        :return: a filtered list with needed objects
        """
        return list(filter(lambda kitchen: kitchen.capacity > capacity, self.kitchens))

    @staticmethod
    def main():

        """
        A main function which adds objects to array and then prints it in different ways
        """

        manager = KitchenManager()
        manager.add_kitchen(Restaurant("Kafe-bar Oksana", 10, 23, 20, 5, 6))
        manager.add_kitchen(Restaurant("Kafe-bar Yaryna", 34, 25, 16, 123, 5))

        manager.add_kitchen(Pub("Kolya Kolya", 50, 51, 50, 321))
        manager.add_kitchen(Pub("Alibi", 656, 100, 12, 7443))

        manager.add_kitchen(Pizzeria("Freddy Fazbear`s", 33, 1223, 312, 31, 31, 122))
        manager.add_kitchen(Pizzeria("Chelentano", 33, 4, 743, 71, 1, 4))

        manager.add_kitchen(HomeKitchen("Home", 33, 4, "Gas", "Wink"))
        manager.add_kitchen(HomeKitchen("Not home", 33, 4, "Electrical", "Wink"))

        for kitchen in manager.kitchens:
            print(kitchen)
            print(kitchen.kitchen_type())

        print("All objects bigger than given size: ")
        bigger_size = manager.find_bigger_than(50)
        for kitchen in bigger_size:
            print(kitchen)

        print("All objects with bigger capacity than given capacity: ")
        bigger_capacity = manager.find_bigger_capacity_than(100)
        for kitchen in bigger_capacity:
            print(kitchen)


KitchenManager.main()
