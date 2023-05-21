from classes.home_kitchen import HomeKitchen
from classes.pizzeria import Pizzeria
from classes.pub import Pub
from classes.restaurant import Restaurant


class KitchenManager:
    """
    Class creates an array of objects and helps to call main function
    """
    kitchens = []

    def add_kitchen(self, kitchen):
        """
        Method which adds kitchens to array
        :param kitchen: name of objects in general
        :return: an addition of kitchen to array
        """
        self.kitchens.append(kitchen)

    @staticmethod
    def main():
        """
        A main function which adds objects to array and then prints it
        """
        manager = KitchenManager()
        manager.add_kitchen(Restaurant("Kafe-bar Oksana", 10, 23, 20, 5, 6))
        manager.add_kitchen(Restaurant("Kafe-bar Yaryna", 34, 25, 16, 123, 5))
        manager.add_kitchen(Pub("Kolya Kolya", 23, 4, 31, 321))
        manager.add_kitchen(Pub("Alibi", 656, 6, 12, 7443))
        manager.add_kitchen(Pizzeria("Freddy Fazbear`s", 33, 4, 312, 31, 31, 122))
        manager.add_kitchen(Pizzeria("Chelentano", 33, 4, 743, 71, 1, 4))
        manager.add_kitchen(HomeKitchen("Home", 33, 4, "Gas", "Wink"))
        manager.add_kitchen(HomeKitchen("Not home", 33, 4, "Electrical", "Wink"))

        restaurant = KitchenManager()

        for restaurant in restaurant.kitchens:
            print(restaurant)
            print(restaurant.kitchen_type())


KitchenManager.main()
