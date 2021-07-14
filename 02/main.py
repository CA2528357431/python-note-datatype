# 赋值

a=1
b=[1,2,3]


# 直接赋值其实是将变量指向同一块内存
c = a
print(id(c))
d = b
print(id(d))


# 所以我们可以解释
a=100
print(c)
b[0]=100
print(d)
# a的变值来自于开辟新内存，因此c值由于还指向原内存而不变
# b的变值来自于改变旧内存，因此d值由于还指向此内存而随之改变