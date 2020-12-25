'''斐波那契 http://oj.yangzhu.world/problem/fib
编写函数fib(n)，求斐波那契数列的第n项，作为函数的返回值返回'''
def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
    
for i in range(1,10):
    print(fib(i),end=' ')
