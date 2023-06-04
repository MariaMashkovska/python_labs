from abc import abstractmethod, ABC


class AbstractKitchen(ABC):
    """
    A parent abstract class which have two methods: adding guests and defining kitchen type
    """

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
