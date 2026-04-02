n = int(input())


for _ in range(1, n+1):

    l1 = True
    l2 = True
    l3 = True
    final =''
    s = input()
    
    for i in s:
        match i:
            case 'A':
                if (l1):
                    final += 'D'
                    l1= not l1
                else:
                    l1= not l1
                    if(l2):
                        final += 'D'
                        l2= not l2
                    else:
                        l2= not l2
                        final += 'E'
            
            case 'B':
                if(l2):
                    l2= not l2
                    final += 'D'
                else:
                    l2 = not l2
                    final += 'E'

            case 'C':
                if(l3):
                    l3 = not l3
                    if(l2):
                        l2 = not l2
                        final += 'D'
                    else:
                        l2 = not l2
                        final += 'E'
                else:
                    final += 'E'
                    l3= not l3

    print(final)