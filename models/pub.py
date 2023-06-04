import random

from abstract_class.abstract_kitchen import AbstractKitchen


class Pub(AbstractKitchen):
    """
    Class creates pubs, add guests and choose the type of kitchen
    """

    def __init__(self, name="", capacity=0, size=0, rating=0, max_capacity_of_guests=0, year_of_foundation=0,
                 type_of_drinks="nothing"):
        """
        :param name - set the name of the restaurant
        :param capacity - set current capacity
        :param size - set the size of room im m^2
        :param max_capacity_of_guests - define max capacity of guests
        :param year_of_foundation - set the year of foundation
        :param type_of_drinks - set the type of drinks in place
        """

        super().__init__(name, capacity, size, rating)
        self.max_capacity_of_guests = max_capacity_of_guests
        self.year_of_foundation = year_of_foundation
        self.type_of_drinks = type_of_drinks

    def add_guests(self, guests):
        """
        :param guests:
        :return: multiplication of current capacity of guests and new guests
        """

        if self.max_capacity_of_guests >= self.capacity + guests:
            return self.capacity + guests

        return "There is no place"

    def kitchen_type(self):
        """
        randomly choose an element of kitchen type in array
        :return: randomly chosen variable
        """
        random_variables = random.choice(AbstractKitchen.kitchen_types)
        return "Type of kitchen: " + str(random_variables)

    def __repr__(self):
        """Method prints an object"""
        return f"Restaurant name='{self.name}', " \
               f"capacity={self.capacity}, " \
               f"size={self.size}, " \
               f"rating={self.rating}, " \
               f"max_capacity_of_guests={self.max_capacity_of_guests}, " \
               f"year_of_foundation={self.year_of_foundation}, " \
               f"type_of_drinks={self.type_of_drinks}"

    def __str__(self):
        return f"Restaurant name='{self.name}', " \
               f"capacity={self.capacity}, " \
               f"size={self.size}, " \
               f"rating={self.rating}, " \
               f"max_capacity_of_guests={self.max_capacity_of_guests}, " \
               f"year_of_foundation={self.year_of_foundation}, " \
               f"type_of_drinks={self.type_of_drinks}"

