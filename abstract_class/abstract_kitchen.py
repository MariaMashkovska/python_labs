from abc import abstractmethod, ABC


class AbstractKitchen(ABC):
    __name = None
    __capacity = None
    __size = None

    kitchen_types = ["ukrainian", "polish", "american", "japanese"]

    def __init__(self, name, capacity, size):
        self.name = name
        self.capacity = capacity
        self.size = size

    @abstractmethod
    def add_guests(self, guests):
        pass

    @abstractmethod
    def kitchen_type(self):
        pass
