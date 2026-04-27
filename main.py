
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None
        self.previous = None
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__


class LinkedList:


    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.MaxSize = None
        
        pass

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return 'Head:{}\nTail:{}\nLIST:\n{}'.format(self.head, self.tail, listString)  

    __repr__=__str__

    
    def __len__(self):
        if self._isEmpty():
            return 0
        current = self.head
        count = 0
        while current != None:
            count +=1
            current = current.next

        return count
        pass

    def _isEmpty(self):
        if self.head == None and self.tail == None:
            return True
        return False
        
        pass

    def _isFull(self):
        if self.maxSize == None:
            return False
        
        if len(self) >= self.MaxSize:
            return True
        
        return False

    def __getitem__(self, key):
        if  key <= len(self):
            current = self.head
            count = 1
            while current != None:
                if count == key:
                    return current
                current = current.next
                count +=1

            return None
        else:
            if len(self) < key:
                return None

        pass

    def __setitem__(self, key, value):
       
        if key <= len(self):
            self[key].value = value
        else:
            return None
        pass

    def index(self, node):
        if not isinstance(node, Node):
            return None
        count = 0
        current = self.head
        while current != None:
            if self[count] == node:
                return count
            current = current.next
            count +=1

        return count
        pass

    def clear(self):
        current = self.head

        while current != None:
        
            next = current.next
            current.previous = None
            current.next = None
            current = None
            current = next
        
        self.head = None
        self.tail = None
        return "LinkedList cleared"


    def set_size(self, size, item):
        headNode = Node(item)
        self.head = headNode
        current = self.head
        count = 1
        while count != size:
            newNode = Node(item)
            if count == size:
                current.next = newNode
                current.next.previous = current
                self.tail = current
            else:
                current.next = newNode
                current.next.previous = current
                current = current.next
            count +=1
        
        return self
    
    
    def maxSize(self, maxSize):
        self.MaxSize = maxSize
        

    def append(self, other):
        if self._isEmpty():
            self.head = other
            self.tail = other
        else:
            newNode = other
            current = self.tail
            current.next = newNode
            self.tail = newNode
            self.tail.previous = current

        pass



class Connect4:
    def __init__(self) -> None:
        self.columns = 7
        self.rows = 6
        self.grid = self.createGrid()
        self.visited = []
        self.bl_moves = 0
        self.or_moves = 0
        

        pass
    
    def __str__(self):
        return f'{self.grid}'
    
    __repr__=__str__

    def createGrid(self):
        lst = LinkedList().set_size(self.columns,None)
        count = 1
        while count != self.columns:
            new_lst = LinkedList()
            new_lst.maxSize(self.rows)
            lst[count] = new_lst
            count +=1
        
        return lst
        pass

    def play(self, column, color):

        if color == "Orange":
            self.or_moves +=1
        elif color == "Blue":
            self.bl_moves +=1
        
        
        if self.grid[column].value._isFull() == False:
            newNode = Node(color)
            self.grid[column].value.append(newNode)
            node_height = self.grid[column].value.index(newNode)
            if self.gameState_check(column, node_height, 0, color, newNode) == True:
                return f"{color} won!"
        
            return f"{color} made a move!"
        return "Column is Full!"
        pass

    def vertical_check(self, node, count, color):
        if count >= 4:
            return True
        else:
            if node and node.value == color:
                return self.vertical_check(node.previous, count +1, color)
        
        return False

        pass

   

    def horizontal_check(self,column_pos, node_height, color):
        count = 1

        col = self.grid[column_pos].previous
        
        while col is not None and col.value[node_height] is not None and col.value[node_height].value == color:
            count +=1
            col = col.previous
        
        col = self.grid[column_pos].next
        
        while col is not None and col.value[node_height] is not None and col.value[node_height].value == color:
            
            count +=1
            col = col.next

        
        return count >= 4
    
        pass

    def right_diagonal_check(self,column_pos, node_height, color):
        count = 1

        col = self.grid[column_pos].previous
        prev_height = node_height -1
        while col is not None and col.value[prev_height] is not None and col.value[prev_height].value == color:
            count +=1
            col = col.previous
            prev_height -=1
        
        col = self.grid[column_pos].next
        next_height = node_height + 1
        while col is not None and col.value[next_height] is not None and col.value[next_height].value == color:
            
            count +=1
            col = col.next
            next_height +=1

        
        return count >= 4
    
        pass

    def left_diagonal_check(self,column_pos, node_height, color):
        count = 1

        col = self.grid[column_pos].previous
        prev_height = node_height + 1
        while col is not None and col.value[prev_height] is not None and col.value[prev_height].value == color:
            count +=1
            col = col.previous
            prev_height +=1
        
        col = self.grid[column_pos].next
        next_height = node_height - 1
        while col is not None and col.value[next_height] is not None and col.value[next_height].value == color:
            
            count +=1
            col = col.next
            next_height -=1

        
        return count >= 4
    
        pass

    def grid_clear(self):
        current_lst = self.grid.head
        
        while current_lst != None:
            if current_lst.value is not None:
                current_lst.value.clear()
            current_lst = current_lst.next
        
        return "Board Cleared!"
        pass

    def gameState_check(self, column,  node_height, count, color, node):
        if self.bl_moves + self.or_moves > 6:
            self.grid_clear()
            return self.vertical_check(node, count, color) or self.horizontal_check(column, node_height, color) or self.right_diagonal_check(column, node_height, color) or self.left_diagonal_check(column,node_height, color)
        pass

# lst = LinkedList()
# lst.append(Node(27722))
# lst.append(Node("sksks"))
# lst.append(Node(82827))
# print(lst)
# lst.clear()
# print(lst)

GAME_1 = Connect4()
#print(GAME_1)
# GAME_1.play(2, "Blue")
# GAME_1.play(3, "Blue")
# GAME_1.play(1, "Yellow")
# GAME_1.play(4, "Yellow")
# GAME_1.play(1, "Yellow")
# GAME_1.play(4, "Yellow")
# GAME_1.play(2, "Yellow")
# GAME_1.play(3, "Yellow")



GAME_1.play(1, "Orange")
GAME_1.play(2, "Blue")
GAME_1.play(2, "Orange")
GAME_1.play(3, "Blue")
GAME_1.play(3, "Blue")
GAME_1.play(3, "Orange")
GAME_1.play(4, "Blue")
GAME_1.play(4, "Blue")
GAME_1.play(4, "Blue")
GAME_1.play(4, "Orange")
#print(GAME_1)



# GAME_1.play(1, "Blue")
# GAME_1.play(1, "Blue")
# GAME_1.play(1, "Blue")
# GAME_1.play(1, "Yellow")
# GAME_1.play(2, "Blue")
# GAME_1.play(2, "Blue")
# GAME_1.play(2, "Yellow")
# GAME_1.play(3, "Blue")
# GAME_1.play(3, "Yellow")
# GAME_1.play(4, "Yellow")
