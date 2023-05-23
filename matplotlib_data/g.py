a = [1,2,4,7,10]
b=[]
missing=[]
for i in range(1,11):
    b.append(i)
    if i not in a:
        missing.append(i)
print(missing)


