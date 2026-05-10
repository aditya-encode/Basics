cat_name=[]

while True:
    print("enter the name of cat "+str(len(cat_name) +1)+ ' or (enter nothing to stop) ')
    name = input()
    if name=='':
        break
    cat_name= cat_name+ [name]
for name in cat_name:

    print( name,end=" ",sep=",") 
