rank_t1 = []
rank_t2 = []
rank_final = []

while True:
    try:
        name, t1, t2, final = input().split()

        rank_t1.append((t1,name))
        rank_t2.append((t2,name))
        rank_final.append((final,name))

    except EOFError:
        break

rank_t1.sort()
rank_t2.sort()
rank_final.sort()

print("T1", rank_t1[0][1],rank_t1[1][1],rank_t1[2][1])
print("T2", rank_t2[0][1],rank_t2[1][1],rank_t2[2][1])
print("CHEGADA", rank_final[0][1],rank_final[1][1],rank_final[2][1])