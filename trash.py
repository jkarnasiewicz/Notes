# dict.iteritems(), dict.viewitems()(reflect dict changes)

# CLASSES
# Classes define the structure and behavior of objects

# __new__ is static class method, while __init__ is instance method.
# __new__ has to create the instance first, so __init__ can initialize it

# Instance method - functions which can be called on objects(with self argument)
# instance.number() == Class.number(instance)

# a dictionary or other mapping object used to store an object’s (writable) attributes
object.__dict__

class Fib:                                       
    def __iter__(self):                          
        self.a = 0
        self.b = 1
        return self

    def next(self):                          
        ...
        if self.index >= len(self.data):
            raise StopIteration
        ...