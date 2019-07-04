''' charecter is upper/lower in sting'''
a="Hello World"
new=""
for i in a:#for i in range(len(a)):
    if(i.isupper()):#if(a[i].isupper()):
        new+=(i.lower())
    else:
        new+=(i.upper())
print(new)
