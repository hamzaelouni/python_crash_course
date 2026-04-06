PIP is the package installer for python

⏺ Python files (modules) can contain any of the following:

- Variables/constants — MAX_RETRIES = 3
- Functions — def process(data): ...
- Classes — class MyService: ...
- Type aliases — UserId = str
- Imports — from typing import List
- Module-level code — code that runs on import

Files are modules, not class containers.


---

In many programming languages, you have to specify the type of a variable when you declare it. 
This is not the case with Python, thanks to its dynamically typed nature. Dynamic typing doesn't mean a variable is devoid of a type.
Instead, Python automatically determines the type upon the variable's instantiation.

`A Double-edged Sword: Potential Errors with Dynamic Typing`
* Python's dynamic typing can be both a boon and a bane. On one hand, it offers flexibility and rapid development. On the other, it can lead to potential runtime errors if not handled with care.


`Tuple Data Type`
* Tuples are like lists with one crucial distinction: **they're immutable**. This means once you've created a tuple, you can't modify it. This characteristic is handy when you want your data to remain constant.
To create a tuple, use parentheses (): t = ('first', 'second', 'third')

* A common misconception about tuples is that their entire content is immutable. In reality, it's only the first level of the tuple that's immutable. This means that while you cannot add or remove items from a tuple itself, if the tuple contains mutable objects, such as lists, you can modify the contents of those internal objects.
  
`Set Data Type`
* Ever needed a collection where every item is unique and order doesn't matter? Enter the Set. It ensures that duplicates are not allowed.
* Define a set using curly braces {}
* You can add items, but remember, duplicates are automatically discarded
*  Items in a set need to be hashable, meaning you can't add mutable types like lists
* sets store items in a hash table, so every element must be hashable (i.e., have a fixed hash value that never changes).  Mutable types are not hashable because their content — and thus their hash — could change
*  a tuple containing a list is also unhashable, because its hash depends on its contents

`Dictionary Data Type`
* Dictionaries are perfect when you want to associate names (keys) with values.
* Define a dictionary using curly braces {} with key-value pairs

#### Decorators 
* Decorators in Python are like wrappers that add extra functionality to existing code without modifying it directly.
* Decorators in Python are higher-order functions, meaning they take another function as input, add extra functionality around it, and return the enhanced version.
* Only override __new__ when you need to control object creation itself, not just initialization.


--- 

`cls` is used in class methods to refer to the class itself, whereas `self` is used in instance methods to refer to a specific instance of the class.

---
###  __ new __
 * the object creator  
 * is the method that creates and returns a new instance of a class. It runs before __init__

```
MyClass()                                                                                                                                                                                                                      
→ __new__(cls)   # 1. creates the object (allocates memory)                                                                                                                                                                      
→ __init__(self) # 2. initializes it (sets attributes)
```



##### When to use it: 
1. Singleton — only one instance ever exists
```
class Singleton:
      _instance = None

      def __new__(cls):
          if not cls._instance:                                                                                                                                                                          cls._instance = super().__new__(cls)
          return cls._instance                                                                                                                                                                                                      
a = Singleton()
b = Singleton()
print(a is b)  # True
```
2. Immutable types — you can't use __init__ to modify them

int, str, tuple are immutable — by the time __init__ runs, the value is already fixed. You must use __new__:
```
class PositiveInt(int):                                                                                                                                                                                                            
    def __new__(cls, value):
        if value <= 0:                                                                                                                                                                                   raise ValueError("Must be positive")
        return super().__new__(cls, value)  # value is set here, not in __init__

n = PositiveInt(5)   # works                
n = PositiveInt(-1)  # ValueError 

```
 
3. Controlling which class gets instantiated
```
class Animal:                           
  def __new__(cls, kind):
      if kind == "dog":                                                                                                                                                                                                          
         return super().__new__(Dog)
      return super().__new__(Cat)

class Dog(Animal): pass
class Cat(Animal): pass

a = Animal("dog")                                                                                                                                                                                                                  
print(type(a))  # <class 'Dog'>
```

---

In almost every Python class, the implicit parent is object — the base class of everything in Python.
```
class Configuration:   
      pass

# is exactly the same as:
class Configuration(object):            
      pass
```     


So when you write super().__new__(cls) inside Configuration:
``` 
super() → object
super().__new__(cls) → object.__new__(cls)   
``` 


---

###  `cls(...)  vs super().__new__(cls)`

* `cls(...)`: Calls the full construction process: `__new__ (create) + __init__ (initialize)`
*  `super().__new__(cls)` : Only handles object creation (memory allocation), skipping `__init__`. 
    It's used inside a class definition to control how the object is born.

---






