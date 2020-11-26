'''水仙花数-loop http://oj.yangzhu.world/problem/narcissisticnumber
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身。
（例如：1^3 + 5^3+ 3^3 = 153）请编写程序，
在一行内，按从小到大的顺序输出所有水仙花数，以空格作为分割'''
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
           if i*100+j*10+k==i**3+j**3+k**3:
                print(i*100+j*10+k,end=' ')
