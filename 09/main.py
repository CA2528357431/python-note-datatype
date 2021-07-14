# 切片拷贝法

a = (1, 2, 3)
b = ['x', 'y', 'z']
c = [a, b]
d = c[::]

print(id(c))
print(id(d))
print()
print(id(c[0]))
print(id(d[0]))
print()
print(id(c[1]))
print(id(d[1]))

# 相当于浅拷贝
