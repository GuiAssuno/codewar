n = int(input())

def enable_l1():
    global l1

    if l1 == 'E':
        l1 = 'D' if l1 == 'E' else 'E'
        return 'D'
    else:
        l1 = 'D' if l1 == 'E' else 'E'
        return enable_l2()

def enable_l2():
    global l2

    if l2 == 'E':
        l2 = 'D' if l2 == 'E' else 'E'
        return 'D'
    else:
        l2 = 'D' if l2 == 'E' else 'E'
        return 'E'
    
def enable_l3():  
    global l3

    if l3 == 'D':
        l3 = 'D' if l3 == 'E' else 'E'
        return 'E'
    else:
        l3 = 'D' if l3 == 'E' else 'E3'
        return enable_l2()

while n > 0:
    line = input()
    l1,l2,l3 = 'E','E','E'
    result = ''

    for c in line:
        if c == 'A':
           result += enable_l1()     
        elif c == 'B':
            result += enable_l2()     
        elif c == 'C':
            result += enable_l3()     

    print(result)
    
    n -= 1
    

