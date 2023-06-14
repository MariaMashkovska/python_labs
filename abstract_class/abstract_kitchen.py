from abc import abstractmethod, ABC


class AbstractKitchen(ABC):
    """
    A parent abstract class which have two methods: adding guests and defining kitchen type
    """
    chefs = set()
    kitchen_types = ["ukrainian", "polish", "american", "japanese"]

    def __init__(self, name, capacity, size):
        """
        :param name: set the name of place
        :param capacity: set the capacity of guests inside
        :param size: set the size of place in m^2
        """
        self.name = name
        self.capacity = capacity
        self.size = size

    def __iter__(self):
        return iter(self.chefs)

    def get_attribs_by_type(self, type_of_attrib):
        """
        Return attributes filtered by type of its value
        :param type_of_attrib: Type of attributes
        :return: Dictionary with filtered attributes names and their values
        """
        return {attrib: value for attrib, value in self.__dict__.items() if type(value) == type_of_attrib}

    @abstractmethod
    def add_guests(self, guests):
        """
        An abstract method which should add guests
        """
        pass

    @abstractmethod
    def kitchen_type(self):
        """
        An abstract method which should define kitchen type
        """
        pass
