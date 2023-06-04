import inspect


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
        file.close()
        return func(self, *args, **kwargs)

    return wrapper


def limit_of_cals(func):
    def wrapper(*args, **kwargs):
        if wrapper.counter <= 3:
            wrapper.counter += 1
            return func(*args, **kwargs)

        raise Exception(f"Method '{func.__name__}' has reached the call limit of 3")

    wrapper.counter = 0
    return wrapper
