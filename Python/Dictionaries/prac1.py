birthdays={'alice':'1 april','bob':'dec 12','carol':'mar 4'}

while True:
    print("enter the name(blank to quit)")
    name=input()
    if name=='':
        break

    if name in birthdays:
        print(birthdays[name]+' is birthday of '+name,sep=' ')
    else:
        print("i dont have information about "+name)
        print("what is birthdate of him/her?")
        brday=input()
        if brday=="":
            break
        birthdays[name]=brday
        print("birthday databse updated successfully")