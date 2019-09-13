print('Python', python_version())

print('\ntiming range()')

print('Python', python_version())
print('Hello, World!')

print("some text,", end="")
print(' print more text on the same line')

print('Python', python_version())
print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)

print('Python', python_version())
print('strings are now utf-8 \u03BCnico\u0394é!')

print('and Python', python_version(), end="")
print(' also has', type(bytearray(b'bytearrays')))

print('Python', python_version())
try:
    let_us_cause_a_NameError
except NameError as err:
    print(err, '--> our error message')
