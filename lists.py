#using the list constructor to create a list
cars =list(("nissan","audi","bmw","toyota","mazda","benz"))
print (cars)
print (cars[-2])

print (cars[0:5])

if "toyota" in cars:
    print ("yes toyota is there")

if "Royce" in cars:
    print("yes its there")
else:
    print ("tswayi kayikho")
######################################

friends=["terence",'tendai','mpofu','geogre','michael']
friends[1]="chris"
friends.insert(3,"kevin")
print (friends)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist.append("orange")
print(thislist)

print()