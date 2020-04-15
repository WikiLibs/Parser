print('Hello, World!')
print('Hello, World!')
print("text"); print('print more text on the same line')

print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)


import timeit

n = 10000


def test_range(n):
    for i in range(n):
        print(i)
        pass


def test_xrange(n):
    for i in xrange(n):
        pass

class Test:
    def __init__(self):
        print("Init")

    def Do(self, msg):
        print(msg)
