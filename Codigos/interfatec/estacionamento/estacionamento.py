arr = [""]*15

while True:
    try:
        id = input()

        n = 0
        for c in id:
            n += ord(c)

        if arr[n%15] == "":
            arr[n%15] = id

    except EOFError:
        break

for i,id in enumerate(arr):
    if id != "":
        print(i+1,id)