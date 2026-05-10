def collatz():
    global number
    if number % 2==0:
        number =number//2
        print(number,end=" ")
        return number
    else:
        number=3*number +1
        print(number,end=" ")
        return number
    
try:    
    number= int(input())
    while number!=1:
        collatz()
except ValueError:
    print("u should enter only integer value")
        
