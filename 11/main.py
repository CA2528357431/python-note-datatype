# 拷贝dic

import copy

a=(1,2,3)
b=['x','y','z']
c={'a':a,'b':b}
d=copy.copy(c)
e=copy.deepcopy(c)

print(id(c))
print(id(d))
print(id(e))
print()
print(id(c['a']))
print(id(d['a']))
print(id(e['a']))
print()
print(id(c['b']))
print(id(d['b']))
print(id(e['b']))

c['a']=1
print(d)
print(e)

# 结果同list的拷贝
