from django.http import HttpResponse

def True_False(a,b):
    dict = {} #Empty Dictionary
    for i in range(a,b):
        c = bin(i) #Decimal to binary
        if (c.find("11")==-1):
            dict.update({i:False})
        else:
            dict.update({i:True})
    return dict

a=int(input("Enter the lowest number:"))
b=int(input("Enter the highest number:"))
mydict = True_False(a,b)
print(mydict)



    