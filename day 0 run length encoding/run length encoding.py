#one liner
(lambda arr:print(*[i[0]+str(len(i))for i in "".join([arr[j]+" "if(arr[j]!=arr[j+1])else arr[j] for j in range(len(arr)-1)]).split()],sep=""))(input()+" ")
'''#one liner logic brief
arr=input()+" "
temp=""
for i in range(len(arr)-1):
    temp+=arr[i]
    if(arr[i]!=arr[i+1]):
        temp+=" "
arr=temp
for i in arr.split():
    print(i[0]+str(len(i)),end="")
'''
