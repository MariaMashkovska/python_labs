class Restaurant:
    __instance = None

    def __init__(self, name="", rating=0, max_capacity=0, current_capacity=0):
        self.name = name
        self.rating = rating
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity

    @staticmethod
    def get_instance():
        if not Restaurant.__instance:
            Restaurant.__instance = Restaurant()
        return Restaurant.__instance

    def accept_reservation(self, num_of_guests):
        if self.current_capacity + num_of_guests <= self.max_capacity:
            self.current_capacity += num_of_guests
            return True
        return False

    def remove_reservation(self, num_of_guests):
        self.current_capacity = max(self.current_capacity - num_of_guests, 0)

    def __str__(self):
        return f"Restaurant(name='{self.name}', rating={self.rating}, max_capacity={self.max_capacity}, current_capacity={self.current_capacity})"

