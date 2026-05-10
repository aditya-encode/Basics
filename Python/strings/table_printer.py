import time,sys


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    alt_tab_0=[]
    alt_tab_1=[]
    alt_tab_2=[]
    alt_tab_3=[]

    for i in table:
        alt_tab_0.append(i[0])
        alt_tab_1.append(i[1])
        alt_tab_2.append(i[2])
        alt_tab_3.append(i[3])
    

    text0=(" ".join(alt_tab_0))
    text1=(" ".join(alt_tab_1))
    text2=(" ".join(alt_tab_2))
    text3=(" ".join(alt_tab_3))
    

    print(text0.rjust(25))
    print(text1.rjust(25))
    print(text2.rjust(25))
    print(text3.rjust(25))


try:
    while True:
        printTable(tableData)
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()