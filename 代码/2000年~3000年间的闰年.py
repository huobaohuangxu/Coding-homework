for i in range(2000,3001):
    if(i%400==0)or(i%4==0 and i%100!=0):
        print(i,end=" ")
