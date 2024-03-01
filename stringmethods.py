# strings are imutable , their values cant be changed in place, it will be stored in a new place. 
a = "!!!!!Harry!!!!!"
print(len(a))
print(a.upper())
print(a.lower())     # it will return a new string,it will not change the existing string.
print(a.rstrip("!"))
print(a.replace("Harry", "john"))
print(a.split(" "))
blog = "introduction tO js"
print(blog.capitalize())  # it will convert the initial letter to uppercase and the following letters to lower case.

str1="Welcome to the console!!!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))     # it will bring line to the center
print(a.count("!"))
print(a.endwith("!"))
print(a.endwith("to",4,10))    # checks whether the sliced string ends with a particular character
print(str1.find("t"))
print(str1.index("t"))    # find will return -1 if the string not found and index will return an error if the string is not found.
print(str1.isalnum())
print(str1.isalpha())
print(a.islower())       # returns true if all the characters are lowercased
print(a.isupper())       # returns true if all the characters are uppercased
print(a.isprintable())   # returns true if all the characters in the string are of printable format
print(a.isspace())       # returns true if the string contains white spaces
print(a.swapcase())      # converts uppercase characters to lowercase and vice versa
print(str1.istitle())
print(a.istitle())
print(str1.startswith("Welcome"))
print(str1.title())