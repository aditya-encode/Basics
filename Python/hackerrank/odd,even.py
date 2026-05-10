n=int(input("input here:"))

while n in range(1,101):
    if n%2!=0:
        print("Weird")
        break
    elif n%2==0 and n in range(2,6):
        print("Not Weird")
        break
    elif n%2==0 and n in range(6,21):
        print("Weird")
        break
    elif n%2==0 and n >=20:
        print("Not Weird")
        break


    