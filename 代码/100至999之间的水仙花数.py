from math import *
print()
for i in range(100,1000):
    n1=i//100;n2=(i % 100)//10;n3=i%10
    if (pow(n1,3)+pow(n2,3)+pow(n3,3) == i):
        print(i,end=' ')
