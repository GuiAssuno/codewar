n = int(input())

results = {}
results[1] = 0
results[3] = 6

for i in range(7,102,4):
    results[i] = i*4 - 4 -2 + results[i-4]

if n in results:
    print(results[n])
else:
    print(results[n-2])

