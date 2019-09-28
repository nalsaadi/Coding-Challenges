n= int(input("Number of commands? "))
list1=[]
for i in range(n):
    request= input("Enter your preferred command: ")
    request= request.split()
    if request[0]== "insert":
        i1= int(request[1])
        i2= int(request[2])
        list1.insert(i1,i2)

    elif request[0]== "remove":
        i1= int(request[1])
        list1.remove(i1)

    elif request[0]== "append":
        i1= int(request[1])
        list1.append(i1)

    elif request[0]== "sort":
        list1.sort()

    elif request[0]== "pop":
        list1.pop()

    elif request[0]== "reverse":
        list1.reverse()
print(list1)

