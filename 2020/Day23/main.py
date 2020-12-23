from tqdm import tqdm

with open("inputs.txt") as f:
    data = f.readlines()[0]

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

higest = len(data)

root = Node(int(data[0]))
node = root
for n in data[1:]:
    node.next = Node(int(n))
    node = node.next
node.next = root

target = 100

cur = root
for _ in range(target):
    pick = []
    pic_node = []
    pick.append(cur.next.val)
    pic_node.append(cur.next)
    pick.append(cur.next.next.val)
    pic_node.append(cur.next.next)
    pick.append(cur.next.next.next.val)
    pic_node.append(cur.next.next.next)
    cur.next = cur.next.next.next.next
    dest = cur.val - 1 
    if dest == 0:
        dest = higest
    while dest in pick:
        dest -= 1
        if dest == 0:
            dest = higest
    # print(dest)
    node = cur.next
    while node.val != dest:
        node = node.next
    pic_node[2].next = node.next
    node.next = pic_node[0]
    cur = cur.next

start = cur
while start.val != 1:
    start = start.next
start = start.next
result = ""

for _ in range(len(data)-1):
    result += str(start.val)
    start = start.next

# part 1
print(result)


higest = 1000000

node_dic = {}
root = Node(int(data[0]))
node_dic[int(data[0])] = root
node = root
for n in data[1:]:
    node.next = Node(int(n))
    node_dic[int(n)] = node.next
    node = node.next

for n in tqdm(range(len(data)+1, higest+1)):
    node.next = Node(int(n))
    node_dic[int(n)] = node.next
    node = node.next

node.next = root

target = 10000000

cur = root
for _ in tqdm(range(target)):
    pick = set()
    pic_node = []
    pick.add(cur.next.val)
    pic_node.append(cur.next)
    pick.add(cur.next.next.val)
    pic_node.append(cur.next.next)
    pick.add(cur.next.next.next.val)
    pic_node.append(cur.next.next.next)
    cur.next = cur.next.next.next.next
    dest = cur.val - 1 
    if dest == 0:
        dest = higest
    while dest in pick:
        dest -= 1
        if dest == 0:
            dest = higest
    # print(dest)
    node = node_dic[dest]
    # while node.val != dest:
    #     node = node.next
    pic_node[2].next = node.next
    node.next = pic_node[0]
    cur = cur.next

start = cur
while start.val != 1:
    start = start.next

print(start.next.val * start.next.next.val)