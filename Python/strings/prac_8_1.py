'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]


'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()

'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())



"        HELLO,GUYS       ".rstrip()




def function(n):
    if n==4:
        return n
    else:
        return 2^function(n+1)
        
print(function(2))