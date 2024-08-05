a=[3,2,6,1]
for i in range(len(a)):
    min=a[i]
    for j in range(1,1):#2
        if(a[j]<min):#2<3
            temp = a[i]
            a[i] = a[j]#2
            a[j] = temp
            min=a[i]
            print(a)
        # else:
            # min=a[j]
            # print(a)