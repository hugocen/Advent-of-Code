with open('Day8.txt', 'r') as f:
    data = f.read()
data = data.replace('\n', '')

# Pic 25*6
i = 0
pics = []
min0 = 25*6
ans = 0
while i < len(data):
    d = data[i:i+(25*6)]
    i += (25*6)
    if d.count('0') < min0:
        min0 = d.count('0')
        ans = d.count('1') * d.count('2')
print(ans)

data = list(data)
i = 0
pic = data[i:i+(25*6)]
i += (25*6)
while i < len(data):
    d = data[i:i+(25*6)]
    i += (25*6)
    for j in range(25*6):
        if pic[j] == '2':
            pic[j] = d[j]
# print(''.join(pic))

i = 0
while i < len(pic):
    if i % 25 == 0:
        print()
    if pic[i] =='1':
        print(chr(9608), end='')
    elif pic[i] == '0':
        print(' ', end='')
    i += 1
print()
