n = int(input())
array = [] 

class Node():
    def __init__(self, num):
        self.data = num
        self.next = None
        self.prev = None

class BidList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0
    
    def push_front(self, num):
        tmp_node = Node(num)
        if self.head is None:
            self.head = tmp_node
            self.tail = tmp_node
        else:
            self.head.prev = tmp_node
            tmp_node.next = self.head
            self.head = tmp_node
        self.num_nodes += 1
    
    def push_back(self, num):
        tmp_node = Node(num)
        if self.head is None:
            self.head = tmp_node
            self.tail = tmp_node
        else:
            tmp_node.prev = self.tail
            self.tail.next = tmp_node
            self.tail = tmp_node
        self.num_nodes += 1

    def pop_front(self):
        if self.head is None:
            pass
        elif self.num_nodes == 1:
            print(self.head.data)
            self.head = None
            self.tail = None
            self.num_nodes -= 1
        else:
            print(self.head.data)
            self.head = self.head.next 
            self.head.prev = None
            self.num_nodes -= 1

    def pop_back(self):
        if self.head is None:
            pass
        elif self.num_nodes == 1:
            print(self.tail.data)
            self.head = None
            self.tail = None
            self.num_nodes -= 1
        else:
            print(self.tail.data)
            self.tail = self.tail.prev
            self.tail.next = None
            self.num_nodes -= 1
    
    def size(self):
        print(self.num_nodes)

    def empty(self):
        if self.num_nodes >= 1:
            print("0")
        else:
            print("1")
    
    def front(self):
        print(self.head.data)

    def back(self):
        print(self.tail.data)


BList = BidList()

for _ in range(n):
    tmp = input().split()
    if len(tmp) == 1:
        instruction = tmp[0]
    else:
        instruction = tmp[0]
        num = int(tmp[1])
    
    if instruction == 'push_front':
        BList.push_front(num)
    elif instruction == 'push_back':
        BList.push_back(num)
    elif instruction == 'pop_front':
        BList.pop_front()
    elif instruction == 'pop_back':
        BList.pop_back()
    elif instruction == 'size':
        BList.size()
    elif instruction == 'empty':
        BList.empty()
    elif instruction == 'front':
        BList.front()
    elif instruction == 'back':
        BList.back()