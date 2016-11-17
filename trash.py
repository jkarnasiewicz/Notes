# dict.iteritems(), dict.viewitems()(reflect dict changes)
# iter(), next()

# a dictionary or other mapping object used to store an object’s (writable) attributes
object.__dict__

# class attribute vs instnace attribute


# REST - representational state transfer
# Podejście REST sugeruje przygotowanie struktury adresu URL dopasowanej do struktury danych
# RESTful URLs are very useful for designing CRUD interfaces(Create, Read, Update, and Delete)

# API - Application Programming Interface

# Runing python with -O option, allow to run python without active assertions

math.copysign(1, y)
math.log10(abs(y))





# def take(n, seq):
#     """Returns first n values from the given sequence."""
#     seq = iter(seq)
#     result = []
#     try:
#       for i in range(n):
#           result.append(seq.__next__())
#     except StopIteration:
#         pass
#     return result

# print(take(15, [i for i in range(10)]))


# # Normal version
# def grep(pattern, filenames):
#     for f in filenames:
#         for line in open(f):
#             if pattern in line:
#                 print line,


# # Generator version
# def readfiles(filenames):
#     for f in filenames:
#         for line in open(f):
#             yield line

# def grep(pattern, lines):
#     return (line for line in lines if pattern in line)

# def printlines(lines):
#     for line in lines:
#         print(line)

# def main(pattern, filenames):
#   import pdb
#   pdb.set_trace()
#   lines = readfiles(filenames) # => generator
#   lines = grep(pattern, lines) # => generator expresion
#   printlines(lines)


# main('open', [__file__])