# loops are used for repition
# for loop can iterate over a sequence of iterable objects in python.eg: lists.strings,tuples,sets,etc
# for loop is used extensively.
name = "abhishek"
for j in name:
    print(j)
    if(j=="b"):
        print("this is something special")
colors = ["red","green","blue","yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)
# range()
for k in range(5):    # we will get value from 0 to 4 ... range(start,stop,step)
    print(k)
for k in range(1,9):             # it will print from 1 to 8
    print(k)
for k in range(1,12,3):
    print(k)

# indentation is necessary in loops and branch statements in python.