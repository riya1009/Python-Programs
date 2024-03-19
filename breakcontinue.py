
# print table of 5 till 10
for i in range(1,12): 
    print(" 5 x", i , "=", 5*i)
    if(i==10):
        break
print("loop chhodkr nikl jao")

# continue mtlb iteration chhodkr nikl jao

for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 x",i,"=",5*i)
