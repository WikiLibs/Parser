print('Python' + python_version())
print('Hello, World!')
print('Hello, World!')
print("text"); print('print more text on the same line')

print('Python', python_version())
print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)

print('Python', python_version())
print(type(unicode('this is like a python3 str type')))

import timeit

n = 10000


def test_range(n):
    for i in range(n):
        pass


def test_xrange(n):
    for i in xrange(n):
        pass    
