# 简单可变的拷贝

import copy

a=[1,2,3]
b=copy.copy(a)
c=copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))

# 此时copy、deepcopy都开辟新地址，无差别