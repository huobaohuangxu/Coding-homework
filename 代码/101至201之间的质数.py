import math;n=0
for m in range(101,201,2):
    k=int(math.sqrt(m))
    for i in range(2,k+2):
        if m % i == 0:
            break
        if i == k+1:
            if n % 10 == 0:
                print()
            print('%d'% m,end=' ')
                n+=1
