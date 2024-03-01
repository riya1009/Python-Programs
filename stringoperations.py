names = "riya,siddhartha"
print(names[0:4]) # string slicing
len1 = len(names) # length of string
print(len1)
print(names[:4])
print(names[:])
print(names[0:-3]) # is equivalent to names[0:len(names)-3]
print(names[-3:-6]) # automatically equivalent to len(names - negative index)
