n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
score = a[k-1]
flag = 0
for i in range(0,len(a)):
    if(a[i]>=score and a[i]>0):
        flag+=1
print(flag)
    