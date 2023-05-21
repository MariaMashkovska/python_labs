from abstract_class.abstract_kitchen import AbstractKitchen


class HomeKitchen(AbstractKitchen):
    """
    Class creates home kitchens, add guests and choose the type of kitchen
    """
    type_of_plate = None
    name_of_hood = None

    def __init__(self, name="", capacity=0, size=0, type_of_plate=0, name_of_hood=0):
        """
        :param name - set the name of the restaurant
        :param capacity - set the current capacity of guests
        :param size - set the size of room in m^2
        :param type_of_plate - set the type of plate
        :param name_of_hood - set the name of hood
        """

        super().__init__(name, capacity, size)
        self.type_of_plate = type_of_plate
        self.name_of_hood = name_of_hood

    def add_guests(self, guests):
        """
        :param guests:
        :return: multiplication of current capacity of guests and new guests
        """
        if self.capacity <= 7:
            return self.capacity + guests
        return "Don't want to visit someone else?"

    def kitchen_type(self):
        """
        :return: first type of kitchen in array
        """
        return "Type of kitchen: " + AbstractKitchen.kitchen_types[0]

    def __str__(self):
        """
        Method prints an object
        """
        return f"Home Kitchen name='{self.name}'," \
               f"capacity={self.capacity}, " \
               f"size={self.size}, " \
               f"type of plate={self.type_of_plate}, " \
               f"name of hood={self.name_of_hood}"

