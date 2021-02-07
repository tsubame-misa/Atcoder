n = int(input())
data = [input() for i in range(n)]
data = list(set(data))
data.sort()
for i in range(len(data)):
    if data[i][0] == "!":
        data[i] = data[i][1:]
data.sort()
for i in range(len(data)-1):
    if data[i] == data[i+1]:
        print(data[i])
        exit()
print("satisfiable")
