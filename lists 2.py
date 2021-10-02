cars=["nissan","audi","bmw","toyota","mazda","benz"]
for x in cars:
     print(x)

for i in range(len(cars)):
    print(cars[i])

cars=["nissan","audi","bmw","toyota","mazda","benz"]
i=0
while i < len(cars):
    print(cars[i])
    i+=1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)

newlist2=[x for x in fruits if x !="mango"]
print(newlist2)

newlist3=[x for x in fruits]
print(newlist3)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

thislist.sort(key=str.upper)
print(thislist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]










