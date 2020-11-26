'''一元二次方程求根-if综合-checker http://oj.yangzhu.world/problem/solvequation
从键盘输入一元二次方程的系数（整数），计算方程的根。
如果有2个不同的根，输出这2个根，精确到小数点后2位。(2个根的输出顺序不作限制)
如果有2个相同的根，输出这1个根，精确到小数点后2位。
如果没有根，输出“no root”'''
from math import sqrt
a,b,c=map(int,input().split());
delta=b*b-4*a*c
if delta > 0:
    x1="%.2f"%((-b-sqrt(delta))/(2*a))
    x2="%.2f"%((-b+sqrt(delta))/(2*a))
    print(x1,x2)
elif delta == 0:
    x3="%.2f"%((-b-sqrt(delta))/(2*a))
    print(x3)
else:
    print("no root")
