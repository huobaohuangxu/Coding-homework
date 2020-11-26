'''一元二次方程根性质-算术运算整除 http://oj.yangzhu.world/problem/rootproperty
从键盘输入一元二次方程ax²+bx+c=0的系数a、b、c（输入者保证输入整数且方程一定存在根），
在不计算根x1和x2的情况下，输出（x1+x2）/2的结果和x1∗x2的结果，输出小数点后2位。'''
a,b,c=map(int,input().split());
d=b*b-4*a*c
if d>=0:
    f=("{:.2f}".format((-b/a)/2))
    e=("{:.2f}".format(c/a))
print(f,e)
