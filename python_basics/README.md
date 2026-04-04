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






