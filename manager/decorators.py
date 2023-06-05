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


def rating_validator(exception, mode):
    def decorator(method):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        if mode == "file":
            file_handler = logging.FileHandler('rating_errors.log')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        elif mode == "console":
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        def wrapper(self, minimal_rating):
            if minimal_rating >= 10:
                logger.error("Rating overflow: %s", minimal_rating)
                raise exception("Rating overflow occurred. Minimal rating argument can not be more than 10.")
            if minimal_rating < 0:
                logger.error("Rating cannot be under 0")

            return method(self, minimal_rating)

        return wrapper
    return decorator
