# 简单不可变拷贝

import copy

a = (1, 2, 3)
b = copy.copy(a)
c = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))

# 都不会开辟新内存
