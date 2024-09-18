num=int(input("Enter number:"))
val=str(num)
rev=val[::-1]
if(val==rev):
    print("The num",num,"is palindrome")
else:
    print("Not palindrome")
for i in range(10):
    if(val.count(str(i))>0):
        print(str(i),"appears",val.count(str(i)),"times")