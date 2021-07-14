# 复杂可变拷贝

import copy

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [a, b]
d = [[7,8],c]


# 浅拷贝仅仅对最上层的c进行了拷贝，对于子对象不拷贝，直接指向
e=copy.copy(d)
print(id(d))
print(id(e))
print()
print(id(d[1]))
print(id(e[1]))


print('-'*50)


# 深拷贝对于整个c包括其全部后代对象都进行拷贝
f=copy.deepcopy(d)
print(id(d))
print(id(f))
print()
print(id(d[1]))
print(id(f[1]))
print(id(d[1][1]))
print(id(f[1][1]))

