'''求最小值 http://oj.yangzhu.world/problem/minvalue
编写函数min_n(a,b,*c)求任意个（至少两个）数值的最小值。
例如：min_n(8,2)返回2，min_n(16,1,7,4,15)返回1'''
def min_n(a,b,*c):
    minval=min(a,b)
    if c:
        m=min(c)
        return min(minval,m)
    else:
        return minval

print(min_n(8,2))
print(min_n(16,1,7,4,15))
