tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(t):
    w=[]
    for i in range(len(t)):
        m=0
        for j in t[i]:
            if len(j)> m:
                m=len(j)
        w.append(m)
    
    for i in range(len(t[0])):
        for j in range(len(t)):
            print(t[j][i].rjust(w[j]),end=" ")
        print()

printTable(tableData)
    