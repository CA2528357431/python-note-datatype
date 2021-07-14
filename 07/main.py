# 复杂不可变拷贝

import copy

a = (1, 2, 3)
b = ['x', 'y', 'z']
c = (a, b)
d=copy.copy(c)
e=copy.deepcopy(c)

print(id(c[0]))
print(id(d[0]))
print()
print(id(c[1]))
print(id(d[1]))
# 只拷贝表层，表层拷贝不开辟


print('-'*50)


print(id(c[0]))
print(id(e[0]))
print()
print(id(c[1]))
print(id(e[1]))
# 深层拷贝拷贝全部，其中可变部分开辟，不可变不开辟


# 总之可以理解为
# deepcopy尝试对对象的全部进行拷贝
# 而copy只对表层进行拷贝
# 拷贝遇到可变类型就开辟新空间，遇见不可变类型就不开辟