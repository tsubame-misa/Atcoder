f = open('res.txt', 'r')
lines = f.readlines()
data = []
for s in lines:
    request = list(map(str, s.split()))
    for j in range(len(request)):
        data.append(request[j])
print(data[7913:7920])

a = ""
for i in range(100):
    a += " 1"
print(a)
