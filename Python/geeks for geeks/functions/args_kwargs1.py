#Name: Alice, Age: 25, City: New York

def qwe(**kwargs):
    details=[]
    for k,v in kwargs.items():
        details.append(k+" : "+str(v))
    print(",".join(details))

qwe(Name="alice",Age=25,City="New york")