thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("yes its there")


#unpacking a tuple

(green,yellow,red)=thistuple
print(green,yellow,red)
















list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list1:
    list1.append(list2)

print(list1)
