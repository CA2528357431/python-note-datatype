# dic自带拷贝法

a=(1,2,3)
b=['x','y','z']
c={'a':a,'b':b}
d=c.copy()

print(id(c))
print(id(d))
print()
print(id(c['a']))
print(id(d['a']))
print()
print(id(c['b']))
print(id(d['b']))

# 是copy
