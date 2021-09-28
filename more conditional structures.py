#MULTI WAY

x=12
if x<34:
    print ('smaller')
elif x==12:
    print ("equals 12")
else:
    print ('neither')

#the try/except structure
astr="hello terence"
try:
    istr=int(astr)
except:
    istr=-1
print ("first",istr)

astr="123"
try:
    istr=int(astr)
except:
    istr=-1

print ("second",istr)

rawstr=input("enter a number:")
try:
    ival=int(rawstr)
except:
    ival=-1
if ival>0:
    print("nice work")
else:
    print ("not a number")