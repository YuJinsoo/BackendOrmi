class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init
        self.count = 0
    
    def __str__(self): 
        if self.head.next == None:  # 빈 Linked list일때 문자열
            return '<>'
        curr_node = self.head
        s = ''
        while curr_node.next != None:
            curr_node = curr_node.next
            s += f'{curr_node.data}, '
        s = s[:-2]
        return f'<{s}>'

    # + operator
    def __add__(self, nextLL):
        if isinstance(nextLL, LinkedList) != True:
            raise ValueError('object have to be LinkedList')
        self.tail.next = nextLL.head.next
        self.tail = nextLL.tail
    
    # * operator
    def __mul__(self, nextint):
        if str(nextint).isdigit() == False:
            raise ValueError('잘못된 값입니다. index는 정수만 전달됩니다.')
        

    # [] operator - 음수 인덱스
    def __getitem__(self, index):
        if index >= self.count:
            raise IndexError(f'범위를 넘어선 인덱스입니다. 길이 {self.count}')
        
        curr_node = self.head
        
        if index < 0 :
            calibarte = 0
            while not(calibarte%self.count == 0 and calibarte >= abs(index)):
                calibarte += 1
            index = calibarte + index

        idx = 0
        while curr_node.next != None:
            curr_node = curr_node.next
            if index == idx:
                return curr_node
            idx += 1
            
    def __iter__(self):
        curr_node = self.head
        curr_node = curr_node.next
        while curr_node:
            yield curr_node.data
            curr_node = curr_node.next

    def __len__(self):
        return self.count

    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode    # 생성전 마지막node가 생성된 node를 가리키게 함
        self.tail = newNode         # 새로 생성된 node를 가리킨다
        self.count +=1
    
    def insert(self, data, index):
        if index > self.count:
            raise IndexError('잘못된 인덱스입니다. 범위를 벗어났습니다.')
        if str(index).isdigit() == False:
            raise ValueError('잘못된 값입니다. index는 정수만 전달됩니다.')
        print('hihihihihiih')
        ins_node = Node(data)
        pre_node = self[index-1]
        curr_node = self[index]
        pre_node.next = ins_node
        ins_node.next = curr_node


    def pop(self, index = None): # int 인자 주면 해당 index pop 해서 제거. 아니면 맨 뒤 제거
        if index == None: ## 맨 뒤 제거
            last_data = self.tail.data
            curr_node = self.head
            for i in range(self.count):
                if curr_node.next is self.tail:
                    self.tail = curr_node
                    curr_node.next = None
                    break;
                curr_node = curr_node.next
            self.count -= 1
            return last_data
        else:   ## 인덱스 요소 제거
            if str(index).isdigit() == False:
                raise ValueError('index는 정수(int)만 전달할 수 있습니다.')
            
            if index < 0 :
                calibarte = 0
                while not(calibarte%self.count == 0 and calibarte >= abs(index)):
                    calibarte += 1
                index = calibarte + index
            
            if index >= self.count:
                raise IndexError('범위를 넘어선 인덱스입니다.')

            curr_node = self.head.next
            pre_node = self.head
            for i in range(self.count):
                if i == index:
                    if curr_node.next == None: ## 일치하는게 마지막 원소일떄
                        pre_node.next = None
                        curr_node = None
                        self.tail = pre_node
                        break
                    else:
                        pre_node.next = curr_node.next
                        curr_node = curr_node.next
                else:
                    pre_node = curr_node
                    curr_node = curr_node.next
                    
            self.count -= 1

    def find(self, data): # 못찾으면 -1 반환
        index = -1
        curr_node = self.head
        for i in range(self.count):
            if curr_node.data == data:
                return index
            index += 1
            curr_node = curr_node.next
        return index
    
    # data를 가진요소를 삭제
    def delete(self, data):
        if self.head.next == None:
            return None
        
        curr_node = self.head.next
        pre_node = self.head
        for i in range(self.count):
            if curr_node.data == data:
                if curr_node.next == None: ## 일치하는게 마지막 원소일떄
                    pre_node.next = None
                    curr_node = None
                    self.tail = pre_node
                    break;
                else:
                    pre_node.next = curr_node.next
                    curr_node = curr_node.next
            else:
                pre_node = curr_node
                curr_node = curr_node.next
        self.count -= 1



ll = LinkedList()
print('빈리스트 : ', ll)

ll.append(10)
ll.append(20)
ll.append(30)
print(ll)

ll.delete(30)
print(ll, ll.count)

ll.append(30)
ll.append(40)
print(ll, ll.count)

print(ll[0], ll[-1], ll[-4], ll[-5], ll[-10])

print(ll.insert(50, 3))
print(ll)