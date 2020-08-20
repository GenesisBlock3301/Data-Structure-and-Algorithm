vowels = ['a','e','i','o','u',"A","E","I",'O',"U","Y",'y']
st = input()
string = ""
for i in st:
    if i in vowels:
        string+=""
    elif i.isupper():
        string+="."+i.lower()
    else:
        string+="."+i
print(string)