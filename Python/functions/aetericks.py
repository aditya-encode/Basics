import sys,time
indent= 0
indent_inc=True

while True:
        try:
                
            print(" "*indent+"*****")
            time.sleep(0.5)
            if indent_inc:
                indent=indent+1
                if indent==5:
                        indent_inc=False
            else:
                indent=indent-1
                if indent==0:
                        indent_inc=True
        except KeyboardInterrupt:
              sys.exit()
              
        
                    


