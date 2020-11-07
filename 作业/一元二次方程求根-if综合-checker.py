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
