a,b,c=map(int,input().split());
d=b*b-4*a*c
if d>=0:
    f=("{:.2f}".format((-b/a)/2))
    e=("{:.2f}".format(c/a))
print(f,e)
