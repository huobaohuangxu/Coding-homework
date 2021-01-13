'''求和-contbreak http://oj.yangzhu.world/problem/continuesum
使用循环和break以及continue完成下面的程序。
从键盘输入若干整数（整数的数目不确定），计算这些数中不是7的倍数的数的和，并输出。
当遇到输入的数是0的时候，停止。'''
a=0
while True:
    i=int(input())
    if i == 0:
        break
    if i % 7 ==0:
        continue
    a+=i
print(a)
