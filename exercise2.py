# to write a program and greet user according to the time
import time
timestamp = time.strftime('%H:%M:%S')    # this function of module gives the current time according to the local computer and returns hours minutes and seconds in string format
print(timestamp)
t1 = time.strftime('%H')                 # giving hours
t2 = time.strftime('%M')                 # giving minutes
t3 = time.strftime('%S')                 # giving seconds 
if(int(t1)>=00):
    if(int(t1)<12):
        print("good morning")
    elif(int(t1)>=12 and int(t1)<5):
        print("good aftenoon")
    elif(int(t1)>=5 and int(t1)<24):
        print("good evening")
else:
    print("not a time in our zone")
print("have a great day ahead")
