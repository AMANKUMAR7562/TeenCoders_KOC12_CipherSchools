a=int(input("any n number:"))
b=[]
c=[]
for i in range(2,10000):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
        else:
            continue
    if(count<=2):
        b.append(i)
for k in b:
    m=k
    reversed_num=0
    while k!=0:
        digit=k % 10
        reversed_num = reversed_num * 10 + digit
        k//=10
    if(m==reversed_num):
        c.append(m)
    else:
        continue
print(c[a-1])
