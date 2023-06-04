import inspect
import logging


def write_attribs_in_file(func):
    """
    Write in file function name, arguments and their values
    """

    def wrapper(self, *args, **kwargs):
        with open("results.txt", "w") as file:
            parameter_names = list(inspect.signature(func).parameters.keys())
            for index, argument in enumerate(args, 1):
                file.write(f"{func.__name__}:{parameter_names[index]}={argument}\n")
            for key, value in kwargs.items():
                file.write(f"{func.__name__}: {key}={value}\n")
        return func(self, *args, **kwargs)

    return wrapper


def limit_of_cals(func):
    """
    Set the limits of 3 function calls
    """

    def wrapper(*args, **kwargs):
        if wrapper.counter <= 3:
            wrapper.counter += 1
            return func(*args, **kwargs)

        raise Exception(f"Method '{func.__name__}' has reached the call limit of 3")

    wrapper.counter = 0
    return wrapper


def logged(exception, mode):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if mode == "console":
        handler = logging.StreamHandler()
    elif mode == "file":
        handler = logging.FileHandler("log.txt")
    else:
        raise ValueError("Invalid mode. Mode should be 'console' or 'file'.")
    logger.addHandler(handler)

    def decorator(func):
        def wrapper(self, *args, **kwargs):
            try:
                # Access fields of the abstract class
                cls = self.__class__
                attributes = inspect.getmembers(cls, lambda a: not inspect.isroutine(a))
                attribute_names = [name for name, _ in attributes]

                # Log the attributes
                logger.info(f"{cls.__name__} attributes: {', '.join(attribute_names)}")

                return func(self, *args, **kwargs)
            except exception as e:
                logger.exception(f"Exception occurred in {func.__name__}: {str(e)}")
                raise

        return wrapper

    return decorator


def rating_validator(func, mode):
    def wrapper(self, *args, **kwargs):
        for kitchen in self.kitchens:
            if kitchen.rating > 10:
                raise Exception("Rating cannot be more than 10.")
        return func(self, *args, **kwargs)

    return wrapper
