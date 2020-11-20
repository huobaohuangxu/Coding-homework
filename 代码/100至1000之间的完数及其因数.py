print()
for n in range(1,1001):
    total=0;j=0;factors=[]
    for i in range(1,n):
        if n % i == 0:
            factors.append(i);total+=i
    if total == n:
        print("{0}:{1}".format(n,factors))
