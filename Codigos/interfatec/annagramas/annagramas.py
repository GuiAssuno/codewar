n  = int(input())

for _ in range(n):
    s1 = input()
    s2 = input()

    n_s1 = len(s1)
    n_s2 = len(s2)

    if n_s2 > n_s1:
        print("ERRO")
        continue

    s2_dict = {}

    for c in s2:
        if c not in s2_dict:
            s2_dict[c] = 0
        
        s2_dict[c] += 1

    s1_dict = {}

    for i in range(n_s2):
        c = s1[i]

        if c not in s1_dict:
            s1_dict[c] = 0
        
        s1_dict[c] += 1

    result = 0

    if s1_dict == s2_dict:
        result += 1

    for i in range(n_s2,n_s1):
        init_c = s1[i-n_s2]
        next_c = s1[i]
        s1_dict[init_c] -= 1

        if s1_dict[init_c] == 0:
            del s1_dict[init_c]

        if next_c not in s1_dict:
            s1_dict[next_c] = 0

        s1_dict[next_c] += 1

        if s1_dict == s2_dict:
            result += 1

    print(result)

