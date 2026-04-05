class Configuration:
    """
    When a new object of this class is instantiated, Python calls the __new__() method.

    The cls passed to this method refers to the class definition,
    which provides access to the class-level _instance attribute.

    cls is used in class methods to refer to the class itself,
    whereas self is used in instance methods to refer to a specific instance of the class.

    At the moment __new__ runs, no instance exists yet — it's the method responsible for creating it.
    So it receives cls (the class) not self (an instance).
    """
    _instance = None  # Class-level attribute to store the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# Testing the Singleton behavior
config1 = Configuration()
config2 = Configuration()

print(config1 is config2)