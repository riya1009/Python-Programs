# anything enclosed in double quotes in python is considered as a string.
name = "riya"
friend = "siddhartha"
apple = 'you are good friend"of mine'
multipleline = ''' you are a good boy
you are good in studies'''
print("hello",friend,apple)
# in python string is like an array of characters 
#index is only from 0 t0 length - 1
print(name[0])
print(name[1])
print(name[2])
print(name[3])
# print(name[4]) will throw an error
print("lets use a for loop to print character in multiple line")
for character in apple:
    print(character, end=" ")

