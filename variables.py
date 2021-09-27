#CASTING
x=str(5)
y=int(5)
z=float(5)
print(x,y,z)
print (type(x))

a,b,c="banana","orange","apple"
print(a)
print(b)
print(c)
#Unpack a Collection
fruits=["apple","banana","cherry"]
b,n,m=fruits
print (b,n,m)

#global variables
d= "awesome "
def myfunc():
    print("python is "+ d)

myfunc()

#local variables
p="awesome"

def pp():
    p="fantastic"
    print ("python is "+p)

pp()

print ('python is'+ p)

#Global keyword

def globe():
    global s
    s= "amazing"
    print ("python is "+ s)
globe()

print ("python is "+ s)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)