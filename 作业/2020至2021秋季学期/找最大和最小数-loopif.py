'''找最大和最小数-loopif http://oj.yangzhu.world/problem/maxmin
从键盘输入1000个整数，找出其中最大的数和最小的数并输出'''
c=a=int(input())
for i in range(1,1000):
    b=int(input())
    if b>a:
        a,b = b,a
    if c>b:
        b,c = c,b
print(a,c)
