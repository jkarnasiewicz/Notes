# iter(), next()
# class attribute vs instnace attribute
# First-Class Functions
# __prepare__
# __getattribute__(self, name)
# __new__(cls, clsname, bases, clsdict)

# interative mode with file_name.py
# python -i file_name.py

# import inspect
# inspect.getsource(object_name)

# Metaprogramming - in a nutshell, code that manipulates code(e.g. decorators, metaclasses, descriptors)
# (extensively used in frameworks and libraries, better understanding of how python works)

# Decorator is a function that creates a wrapper around another function

# Metaclasses propagate down hierarchies (genetic mutation - wszystkie klasy które dziedziczą po Base będą mieć 'metaclass=mytype')
# class Base(metaclasses=mytype):
#     pass

# Descriptors - customized processing of attribute access (dostosowany/zindywidualizowany proces dostępu do atrybutu)

# keyword-only args
# TypeError: fun() missing 1 required keyword-only argument: 'post'
# def fun(*args, post, **kwargs): pass
# fun(1, 2, 'st', p=33, k=44, j='o')
