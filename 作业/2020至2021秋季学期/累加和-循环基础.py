'''累加和-循环基础 http://oj.yangzhu.world/problem/cumulativesum
从键盘输入两个整数，计算这2个整数（不含）之间所有整数之和。'''
a,b=map(int,input().split())
sum_all=0
for a in range(a+1,b):
    sum_all+=a
print(sum_all)
