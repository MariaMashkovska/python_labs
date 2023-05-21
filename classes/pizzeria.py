from abstract_class.abstract_kitchen import AbstractKitchen


class Pizzeria(AbstractKitchen):
    """
    Class creates home pizzerias, add guests and choose the type of kitchen
    """
    year_of_foundation = None
    type_of_drinks = None
    capacity_of_seats = None
    capacity_of_animatronics = None

    def __init__(self, name="", capacity=0, size=0, year_of_foundation=0,
                 type_of_drinks="nothing", capacity_of_seats=0, capacity_of_animatronics=0):
        """
        :param name - set the name of the restaurant
        :param capacity - set the current capacity of guests
        :param size - set the size of room in m^2
        :param capacity_of_seats - define max capacity of guests
        :param year_of_foundation - set the year of foundation
        :param type_of_drinks - set the type of drinks in place
        """

        super().__init__(name, capacity, size)
        self.year_of_foundation = year_of_foundation
        self.type_of_drinks = type_of_drinks
        self.capacity_of_seats = capacity_of_seats
        self.capacity_of_animatronics = capacity_of_animatronics

    def add_guests(self, guests):
        """
        :param guests:
        :return: multiplication of current capacity of guests and new guests
        """
        if self.capacity_of_seats >= self.capacity + guests:
            return self.capacity + guests

        return "There is no place"

    def kitchen_type(self):
        """
        :return: third type of kitchen in array
        """
        return "Type of kitchen: " + AbstractKitchen.kitchen_types[2]

    def __str__(self):
        """
        Method prints an object
        """
        return f"Home Kitchen name='{self.name}'," \
               f"capacity={self.capacity}, " \
               f"size={self.size}, " \
               f"year_of_foundation={self.year_of_foundation}, " \
               f"type_of_drinks={self.type_of_drinks}, " \
               f"capacity_of_seats={self.capacity_of_seats}, " \
               f"capacity_of_animatronics={self.capacity_of_animatronics}"

