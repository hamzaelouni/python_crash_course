def singleton(cls):
    # Creates an empty dictionary _instance inside singleton.
    # It will store the one and only instance of the class.
    # The _ prefix is a Python convention meaning "private/internal use".
    _instance = {}

    # *args collects positional arguments, **kwargs collects keyword arguments — meaning it accepts any arguments you pass.
    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return wrapper

@singleton
class Configuration:
    # pass means the class body is empty.
    pass

# Testing the Singleton behavior
config1 = Configuration()
config2 = Configuration()

#  is checks if both variables point to the exact same object in memory
print(config1 is config2)