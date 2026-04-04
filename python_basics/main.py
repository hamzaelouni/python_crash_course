x = "test"
print(type(x))  # This will return <class 'str'>

y = 1
print(type(y)) # This will return <class 'int'>

# While the original type of y was an integer, reassigning it to a floating-point number changed its type dynamically.
y = 1.0
print(type(y))  # This will return <class 'float'>


#result = x + y
#print(result) # Throws a TypeError exception, can only concatenate str (not "float") to str

# create a list
l = ['first', 'second']
print(type(l)) # This will return <class 'list'>

l.append('fourth')     # Adds 'fourth' to the end
l.insert(2, 'third')  # Inserts 'third' at position 3
l.remove('first')     # Removes the 'first' item
print(l)

# create a tuple
t_0 = ('first', 'second', 'third')
t_1 = ([1, 2], [4, 5, 6])

t_1[0].append(3)
print(t_1)  # Outputs ([1, 2, 3], [4, 5, 6])

# create a set
s = {1, 2, 3}
s.add(4)
s.add(3)  # No effect, as 3 is already in the set
print(s) # Outputs {1, 2, 3, 4}

# This raises an error:
#s = {[1,2,3], [4,5,6]}
#print(s) # throws => TypeError: unhashable type: 'list'

s = {(1, 2, 3)}       # tuple — works
s = {frozenset([1,2])} # frozenset — works

d = {"item": "laptop", "quantity": 10, "price": 400.00}
print(d["item"])