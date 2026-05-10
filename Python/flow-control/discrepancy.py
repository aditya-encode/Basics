print("enter the unit :")
unit = input()

if unit == 'GB' or unit== 'gb':
    discrepancy = 1000000000/1073741824
elif unit == "TB" or unit== "tb":
    discrepancy = 1000000000000/1099511627776

print("enter the advertised capacity")
advertised_capacity =input()
advertised_capacity=float(advertised_capacity)

real_capacity= str(round(advertised_capacity *discrepancy,2 ))

print('the actual capacity is '+ real_capacity+unit)