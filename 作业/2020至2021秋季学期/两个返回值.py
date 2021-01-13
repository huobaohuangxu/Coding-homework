'''两个返回值 http://oj.yangzhu.world/problem/tworetval
Python 3
编写如下函数，同时返回a、b之和以及a、b之差
tworetval(a, b)

C、C++
编写如下函数，实现同时返回参数a和b的和与差，和放在addval指向的位置，差放在subval指向的位置
void tworetval(int a, int b, int *addval, int *subval
'''
def tworetval(a,b):
    x=a+b
    y=a-b
    return x,y
    
print(a,b)
