#求圆面积-初学者常见错误 http://oj.yangzhu.world/problem/circlearea
#圆周率取3.1415926，从键盘输入圆的半径（可以是整数、也可以是浮点数），计算并输出圆的面积，输出到小数点后10位，至少精确到小数点后10位。
PI=3.1415926
r=float(input())
s=PI*r*r
print("{0:.10f}".format(s))
