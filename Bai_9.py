list=[1,2,4,4,7,8,1,9,5,3,3,4,11]
result=[]
for i in list:
    if i not in result:
        result.append(i)
result.sort()
print(result)


