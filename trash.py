# dict.iteritems(), dict.viewitems()(reflect dict changes)
# iter(), next()



# CLASSES
# Classes define the structure and behavior of objects

# __new__ is static class method, while __init__ is instance method.
# __new__ has to create the instance first, so __init__ can initialize it

# Instance method - functions which can be called on objects(with self argument)
# instance.number() == Class.number(instance)

# a dictionary or other mapping object used to store an object’s (writable) attributes
object.__dict__


class Container(object):

    def __init__(self, sequence):
        self.sequence = sequence

    # def __iter__(self):
    #     # for i in self.sequence:
    #     #     yield i
    #     # print(type(self.sequence))
    #     # print(type(iter(self.sequence)))
    #     # return iter(self.sequence)
    #     return iter(self.sequence)




    # def __next__(self):
    #     # for i in self.sequence:
    #     #     yield i
    #     return iter(self.sequence)


cont = Container([1, 2, 3, 5])

for i in cont:
    print(i)
