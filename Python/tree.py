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
        
        while curr_node:
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
    
    def get_childrens_data(self, node):
        result = []
        new_root = node
        stack = [new_root]
        
        while stack:
            curr = stack.pop(0)
            result.append(curr.data)
            
            if curr.left != None:
                stack.append(curr.left)
                
            if curr.right != None:
                stack.append(curr.right)
                
        
        return result
    
    def get_parent(self, node):
        result = 0
        stack = [self.root]
        
        while node not in stack:
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
    
    def get_parent_data(self, node):
        result = 0
        stack = [self.root]
        
        while node not in stack:
            curr = stack.pop()
            
            if curr.left != None :
                stack.append(curr.left)
                if curr.left == node:
                    result = curr.data
            
            if curr.right != None:
                stack.append(curr.right)
                if curr.right == node:
                    result =  curr.data
                
        return result
    
    def left_child(self):
        return self.left
    
    def right_child(self):
        return self.right
    
    def remove(self, node):
        
        if node.left == None and node.right == None:
            parent = self.get_parent(node)
            if parent.data < node.data:
                parent.right = None
            elif parent.data > node.data:
                parent.left = None
        
        if node.left != None and node.right == None:
            maximum = max(self.get_childrens_data(node))
                
    
    def find(self, data):
        result = None
        curr = self.root
        
        while curr != None:
            if curr.data == data:
                result = curr
                break
                # curr = None # break
            elif curr.data > data:
                curr = curr.left
            elif curr.data < data:
                curr = curr.right
                
        return result
    
    def DFS(self):
        result = []
        stack = [self.root]
        
        while stack:
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
        
        while queue:
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

print(t.get_childrens_data(t.root.left))
print(t.get_childrens_data(t.root.right))
print(t.get_parent_data(t.root.left))
print(t.get_parent_data(t.root.left.right))

print(t.find(3).data)







