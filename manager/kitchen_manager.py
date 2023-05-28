from models.home_kitchen import HomeKitchen
from models.pizzeria import Pizzeria
from models.pub import Pub
from models.restaurant import Restaurant

import inspect


def write_attribs_in_file(func):
    """
    Write in file function name, arguments and their values
    """

    def wrapper(self, *args, **kwargs):
        with open("results.txt", "w") as file:
            parameter_names = list(inspect.signature(func).parameters.keys())
            for index, argument in enumerate(args, 1):
                file.write(f"{func.__name__}:{parameter_names[index]}={argument}\n")
            for key, value in kwargs.items():
                file.write(f"{func.__name__}: {key}={value}\n")
        return func(self, *args, **kwargs)

    return wrapper


def limit_of_cals(func):
    def wrapper(*args, **kwargs):
        if wrapper.counter <= 3:
            wrapper.counter += 1
            return func(*args, **kwargs)
        else:
            raise Exception(f"Method '{func.__name__}' has reached the call limit of 3")

    wrapper.counter = 0
    return wrapper


class KitchenManager:
    """
    Class creates an array of objects and helps to call main function
    :param kitchens - an array of abstract class`s children objects
    """
    kitchens = []

    @write_attribs_in_file
    def add_kitchen(self, kitchen):
        """
        Method which adds kitchens to array
        :param kitchen: name of objects in general
        :return: an addition of kitchen to array
        """
        self.kitchens.append(kitchen)

    @write_attribs_in_file
    def find_bigger_than(self, size):
        """
        Method finds all objects bigger than given size
        :param size: of place
        :return: a filtered list with needed objects
        """
        return list(filter(lambda kitchen: kitchen.size > size, self.kitchens))

    @write_attribs_in_file
    def find_bigger_capacity_than(self, capacity):
        """
        Method finds all objects with bigger capacity than given size
        :param capacity: of possible people in place
        :return: a filtered list with needed objects
        """
        return list(filter(lambda kitchen: kitchen.capacity > capacity, self.kitchens))

    def __len__(self):
        """
        Returns the number of kitchens in the manager
        """
        return len(self.kitchens)

    def __getitem__(self, index):
        """
        Returns the kitchen at the specified index
        """
        return self.kitchens[index]

    def __iter__(self):
        """
        Returns an iterator over the kitchens in the manager
        """
        return iter(self.kitchens)

    @limit_of_cals
    def type_of_kitchens(self):
        """
        :return: Type of kitchen for every kitchen
        """
        return [kitchen.kitchen_type() for kitchen in self.kitchens]  # TODO check kitchen_type(), why random?

    @limit_of_cals
    def enumerate_concatenation(self):
        """
        Returns a concatenation of each kitchen object and its index in the manager
        """
        return list(enumerate(self.kitchens))

    @limit_of_cals
    def zip_concatenation(self):
        """
        Returns a concatenation of each kitchen object and the result of the kitchen_type() method
        """
        return list(zip(self.kitchens, self.type_of_kitchens()))

    @limit_of_cals
    @write_attribs_in_file
    def rating_check(self, minimal_rating):
        """
        Checks if all objects in the manager satisfy the given condition
        """
        result = [kitchen.rating > minimal_rating for kitchen in self.kitchens]
        return {
            "all": all(result),
            "any": any(result)}


class SetManager:
    """
    Class to work with chefs inside every kitchen
    """
    all_chefs = []

    def __init__(self, regular_manager):
        """
        Put chefs from all kitchens in one list
        :param regular_manager: object type Manager
        """
        self.all_chefs = [chef for kitchen in regular_manager.kitchens for chef in kitchen]

    def __getitem__(self, item):
        return self.all_chefs[item]

    def __iter__(self):
        return iter(self.all_chefs)

    def __len__(self):
        return len(self.all_chefs)

    def __next__(self):
        return next(self.__iter__())


manager = KitchenManager()
manager.add_kitchen(Restaurant("Kafe-bar Oksana", 10, 23, 2, 5, 6))
manager.add_kitchen(Restaurant("Kafe-bar Yaryna", 34, 25, 16, 123, 5))

print(manager.type_of_kitchens())
print(manager.enumerate_concatenation())
print(manager.zip_concatenation())
print(manager.kitchens[0].get_attribs_by_type(str))  # absract_kitchen.py
print(manager.rating_check(4))  # Як я зрозумів, назва методу і сама умова може бути яка захочеш, тому я вибрав таке, всі інше по методичці

set_manager = SetManager(manager)
print(set_manager.all_chefs)
print(len(set_manager))
for i in set_manager:
    print(i)
print(set_manager[0])

# manager.add_kitchen(Pub("Kolya Kolya", 50, 51, 50, 321))
# manager.add_kitchen(Pub("Alibi", 656, 100, 12, 7443))
#
# manager.add_kitchen(Pizzeria("Freddy Fazbear`s", 33, 1223, 312, 31, 31, 122))
# manager.add_kitchen(Pizzeria("Chelentano", 33, 4, 743, 71, 1, 4))
#
# manager.add_kitchen(HomeKitchen("Home", 33, 4, "Gas", "Wink"))
# manager.add_kitchen(HomeKitchen("Not home", 33, 4, "Electrical", "Wink"))
#
# for kitchen in manager.kitchens:
#     print(kitchen)
#     print(kitchen.kitchen_type())
#
# print("\nAll objects bigger than given size: ")
# bigger_size = manager.find_bigger_than(50)
# for kitchen in bigger_size:
#     print(kitchen)
#
# print("\nAll objects with bigger capacity than given capacity: ")
# bigger_capacity = manager.find_bigger_capacity_than(100)
# for kitchen in bigger_capacity:
#     print(kitchen)
#
# print("\nConcatenation of each kitchen object and its index:")
# print(manager.enumerate_concatenation())
#
# print("\nConcatenation of each kitchen object and the result of the do_something() method:")
# print(manager.zip_concatenation())
#
# print("\nAttributes of the objects with value type int:")
# print(manager.attribute_dict(int))
#
# print("\nCheck if all objects satisfy the condition:")
# print(manager.all_any_check(lambda kitch: kitchen.size > 10))
#
# print("\nCheck if any object satisfies the condition:")
# print(manager.all_any_check(lambda kitch: kitchen.capacity > 300))
