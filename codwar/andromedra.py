import sys 
import io 
import time
entrada = """123456789
900900900
987654321
"""

x = []
sys.stdin = io.StringIO(entrada)

#print (len(sys.stdin.readlines()))

while True:
    try:
        a = input()
    except:
        break

    for y in a:
        x.append (y)
    
    for i in range(1,len(x)+1):
        
        print(x[-i], end="")
    print()
    x=[]