import random,time,sys
WIDTH=70

try:
    while True:
        column=[0]*WIDTH
        for i in range(WIDTH):
            if random.random()<0.02:
                column[i]=random.randint(4,14)
            
            if column[i]==0:
                print(" ",end='')
            else:
                print(random.choice([0,1]),end='')
                column[i]-=1
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()

