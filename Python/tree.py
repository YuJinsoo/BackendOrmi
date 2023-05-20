class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self, data):
        init = Node(data)
        self.root = init
        self.count = 1
        
    def __len__(self):
        return self.count
    
    def __str__(self):
        
        t = self.BFS()
        
        return f'Tree {t}'
    
    def insert(self, data):
        new_node = Node(data)
        curr_node = self.root
        
        while curr_node != None:
            if curr_node.data == data:
                return
            elif data < curr_node.data:
                if curr_node.left != None:
                    curr_node = curr_node.left
                else:
                    curr_node.left = new_node
            elif data > curr_node.data:
                if curr_node.right != None:
                    curr_node = curr_node.right
                else:
                    curr_node.right = new_node
    
    # 전체/하위 노드 출력
    def get_childrens(self, node = None): 
        result = []
        
        if node == None:
            node = self.root
            
        new_root = node
        queue = [new_root]
        
        while len(queue) != 0:
            curr = queue.pop(0)
            result.append(curr)
            
            if curr.left != None:
                queue.append(curr.left)
                
            if curr.right != None:
                queue.append(curr.right)
                
        
        return result
    
    # 부모 노드
    def get_parent(self, node):
        result = 0
        stack = [self.root]
        
        while len(stack) != 0:
            if node == self.root:
                break
            curr = stack.pop()
            
            if curr.left != None :
                stack.append(curr.left)
                if curr.left == node:
                    result = curr
            
            if curr.right != None:
                stack.append(curr.right)
                if curr.right == node:
                    result =  curr
                
        return result
    
    # 노드의 깊이
    def get_node_depth(self, node): 
        depth = 0# root를 0으로 하겠습니다.
        curr_node = node
        
        while curr_node != self.root:
            curr_node = self.get_parent(curr_node)
            depth += 1
            
        return depth
    
    def left_child(self):
        return self.left
    
    def right_child(self):
        return self.right
    
    def find(self, data):
        result = None
        curr = self.root
        
        while curr != None:
            if curr.data == data:
                result = curr
                break
            elif curr.data > data:
                curr = curr.left
            elif curr.data < data:
                curr = curr.right
                
        return result
    
    # 제거 미완
    def remove(self, node):
        
        if node.left == None and node.right == None:
            if node == self.root:
                self.root = None
                return
            
            parent = self.get_parent(node)
            if parent.data < node.data:
                parent.right = None
            elif parent.data > node.data:
                parent.left = None
        
        if node.left != None and node.right == None:
            parent = self.get_parent(node)
            maximum = max(self.get_childrens_data(node))
        
        if node.left == None and node.right != None:
            maximum = max(self.get_childrens_data(node))
                
        if node.left != None and node.right != None:
            maximum = max(self.get_childrens_data(node))
                
    
    
    def DFS(self):
        result = []
        stack = [self.root]
        
        while len(stack) != 0:
            curr = stack.pop()
            
            if curr.left != None:
                stack.append(curr.left)
            if curr.right != None:
                stack.append(curr.right)
            
            result.append(curr.data)
        
        return result
    
    def BFS(self):
        result = []
        queue = [self.root]
        
        while len(queue) != 0:
            curr = queue.pop(0)
            
            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)
            
            result.append(curr.data)
        
        return result


t = Tree(5)
t.insert(3)
t.insert(8)
t.insert(1)
t.insert(4)
t.insert(6)
t.insert(9)

print(t.root.data)
print(t.root.left.data)
print(t.root.right.left.data)
print(t.DFS())
print(t.BFS())

for i in t.get_childrens(t.root.left):
    print(i.data, end = ' ')
    
print()
for i in t.get_childrens(t.root.right):
    print(i.data, end = ' ')
    
print()
for i in t.get_childrens():
    print(i.data, end = ' ')

print()
print(t.get_parent(t.root.left).data)
print(t.get_parent(t.root.left.right).data)

print(t.find(3).data)
print(t.find(3).data)

print(t.get_node_depth(t.find(4)))








