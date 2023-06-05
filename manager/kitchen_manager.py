from manager.decorators import write_attribs_in_file, limit_of_cals, rating_validator
from manager.set_manager import SetManager
from models.pizzeria import Pizzeria
from models.restaurant import Restaurant


class RatingOverflowError(Exception):
    pass


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
        :return: random type of kitchen for every kitchen
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

    @write_attribs_in_file
    @limit_of_cals
    @rating_validator(RatingOverflowError, mode="сonsole")
    def rating_check(self, minimal_rating):
        """
        Checks if all objects in the manager satisfy the given condition
        """
        result = [kitchen.rating > minimal_rating for kitchen in self.kitchens]
        return {
            "all": all(result),
            "any": any(result)}


manager = KitchenManager()
manager.add_kitchen(Restaurant("Kafe-bar Oksana", 10, 23, 2, 5, 6))
manager.add_kitchen(Restaurant("Kafe-bar Yaryna", 34, 25, 5, 123, 5))

manager.add_kitchen(Pizzeria("Freddy Fazbear`s", 33, 1223, 8, 31, 31, 122))
manager.add_kitchen(Pizzeria("Chelentano", 33, 4, 1, 71, 1, 4))

print(manager.type_of_kitchens())
print(manager.enumerate_concatenation())
print(manager.zip_concatenation())
print(manager.kitchens[0].get_attribs_by_type(str))
print(manager.rating_check(10))

set_manager = SetManager(manager)
print(set_manager.all_chefs)
print(len(set_manager))
for i in set_manager:
    print(i)
print(set_manager[0])
