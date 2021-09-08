from nltk.corpus import stopwords as sw
#a=int(input(""))
"""k=0
flag=0
for i in range(1,2*a):
    if i%2==0:
        start=i-k
        end=0
        diff=-1
    else:
        start=1
        end=i+1-k
        diff=1

    for j in range(start,end,diff):
        print(j, end=",")
    print()
    if i==a:
        flag=1
    if flag==1:
        k+=2"""
print(bool("kahs"))
a="abhishek"
b="ab"
print(b in a)
list=["this","punit","is","punit","that","punit","that","abhishek","ran","punit","is"]
stops = sw.words('english')
for i in list:
    if i in stops:
        list.remove(i)
print(list)