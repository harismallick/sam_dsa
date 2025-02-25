x: int = 10
y = x
print(id(x))
print(id(y))

y = 12
print(id(x))
print(id(y))