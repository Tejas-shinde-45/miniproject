listle=int(input("enterr the length of the list:"))
cnt=0
liste=[]
for i in range(listle):
    lisvl=input("entert the list numbers:")
    liste.append(lisvl)
    cnt +=1
print("list is give by the user",liste)
print("total list count is :",cnt)
liste.sort(reverse=True)
print("decrementing sorting is :",liste)
# list1=sorted(liste,reverse=True)
# print(list1)
ll=0
for i in range(0,cnt):
    for j in range(0,cnt):
        print([liste[i],liste[j]])
        ll+=1

print("lenght of the combinationss:",ll)

