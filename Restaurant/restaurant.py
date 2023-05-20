class Restaurant:
    """
    Class creates restaurants, accept and remove reservation
    """
    __instance = None

    def __init__(self, name="", rating=0, max_capacity=0, current_capacity=0):
        """
           :param name - set the name of the restaurant
           :param rating - set the rating
           :param max_capacity - define max capacity to accept reservation
           :param current_capacity - define current capacity of guests
           """
        self.name = name
        self.rating = rating
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity

    @staticmethod
    def get_instance():
        """Method creates an object"""
        if not Restaurant.__instance:
            Restaurant.__instance = Restaurant()
        return Restaurant.__instance

    def accept_reservation(self, num_of_guests):
        """ Method checks if we can add new guests and then adds them """
        if self.current_capacity + num_of_guests <= self.max_capacity:
            self.current_capacity += num_of_guests
            return True
        return False

    def remove_reservation(self, num_of_guests):
        """ Method deletes guests from current capacity """
        self.current_capacity = max(self.current_capacity - num_of_guests, 0)

    def __str__(self):
        """Method prints an object"""
        return f"Restaurant name='{self.name}'," \
               f" rating={self.rating}, " \
               f"max_capacity={self.max_capacity}, " \
               f"current_capacity={self.current_capacity}"
