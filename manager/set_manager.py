class SetManager:
    """
    Class to work with chefs inside every kitchen
    """
    all_chefs = []

    def __init__(self, regular_manager):
        """
        Put chefs from all kitchens in one list
        :param regular_manager: object type Manager
        """
        self.all_chefs = [chef for kitchen in regular_manager.kitchens for chef in kitchen]

    def __getitem__(self, item):
        return self.all_chefs[item]

    def __iter__(self):
        return iter(self.all_chefs)

    def __len__(self):
        return len(self.all_chefs)

    def __next__(self):
        return next(self.__iter__())