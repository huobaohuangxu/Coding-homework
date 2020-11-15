#九九乘法表-循环嵌套 http://oj.yangzhu.world/problem/haskell
#输出九九乘法表的左下三角
for i in range(1,10):
    for j in range(1,i+1):
        print('{0}*{1}={2} '.format(i,j,'%2d'%(i*j)),end=" ")
    print()
