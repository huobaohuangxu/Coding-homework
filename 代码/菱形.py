n=int(input('请输入上（或下）三角的行数：'))
for i in range(0,n):
    print(''.rjust(19-i),end='')
    for j in range(2*i+1):print('*',end='')
    print('\n')
for i in range(n-1,0,-1):
    print(''.rjust(19-i),end='')
    for j in range(2*i-1):print('*',end='')
    print('\n')
