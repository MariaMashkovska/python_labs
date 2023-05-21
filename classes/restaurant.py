import random

from abstract_class.abstract_kitchen import AbstractKitchen


class Restaurant(AbstractKitchen):
    """
    Class creates restaurants, accept, remove reservation, add guests and choose the type of kitchen
    """
    rating = None
    max_capacity = None
    current_capacity = None

    def __init__(self, capacity=0, size=0, name="", rating=0, max_capacity=0, current_capacity=0):
        """
        :param name - set the name of the restaurant
        :param capacity - set the current capacity of guests
        :param size - set the size of room in m^2
        :param rating - set the rating
        :param max_capacity - define max capacity to accept reservation
        :param current_capacity - define current capacity of guests
        """
        super().__init__(name, capacity, size)
        self.rating = rating
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity

    def accept_reservation(self, num_of_guests):
        """
        Method checks if we can add new guests and then adds them
        """
        if self.current_capacity + num_of_guests <= self.max_capacity:
            self.current_capacity += num_of_guests
            return True
        return False

    def remove_reservation(self, num_of_guests):
        """
        Method deletes guests from current capacity
        """
        self.current_capacity = max(self.current_capacity - num_of_guests, 0)

    def kitchen_type(self):
        """
        randomly choose an element of kitchen type in array
        :return: randomly chosen variable
        """
        random_variables = random.choice(AbstractKitchen.kitchen_types)
        return "Type of kitchen: " + str(random_variables)

    def add_guests(self, guests):
        """
        :param guests:
        :return: multiplication of current capacity of guests and new guests
        """
        if self.max_capacity >= self.capacity + guests:
            return self.capacity + guests

        return "There is no place"

    def __str__(self):
        """Method prints an object"""
        return f"Restaurant name='{self.name}'," \
               f"capacity={self.capacity}, " \
               f"size={self.size}, " \
               f"rating={self.rating}, " \
               f"max_capacity={self.max_capacity}, " \
               f"current_capacity={self.current_capacity}"
