a,b=0,1
for i in range(1,21):
    a,b=b,a+b
    print('{0:6d}'.format(a),end=" ")
    if i % 4==0:
        print()
