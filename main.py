import tkinter as tk
import base64

root = tk.Tk()
root.title("Connect4 in Python!")


board64_string = "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"
logo64_string = "iVBORw0KGgoAAAANSUhEUgAAAj0AAACoCAYAAAALpV/YAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAI2klEQVR4nO3d0ZHjRBAGYAtUkACkdaQAQUAQXBBcClwMZAPPWwV1lKg7yovr0K4lazTTM/19L1Ds4pXGljX6uzWalmW5AADbTNPkxHnHzdxiugTyResNAACowaQHAEhhbr0BANBrWUuLyLppeq5qrY1Zs5KXpAcASGEySwWAddKdU9KfZg3Pkh4AIAWTHgAgBY3MALDB3rLWWjkn87gsK7+31vB8ZqOzpAcASEHSAwD/93C3cpaEZ8v+3kuBrj+vNWaSHgAgBZMeACAF6/QAwAvr82w9R2YraT3itbF8YQ2f4oMq6QEAUtDIDAD/2l36kPDsH6u1xOf2v505ppIeACAFkx4AIAXlLQD4rKyyt+mW8uN8BkkPAJCCpAeA1K63pzM+SQ8AkIJJDwCQgvIWAGxoqtXA3D9JDwCQgqQHgJEsJZOZ2unOV9//XPT1/vzlx0///PqHt5ez/PXup0svJD0AQAomPQBAClXKW9ZAAKC22qv9Ep+kBwBIYa6Z6ph1A9CDmg3MpZuXjzQ8rzmzCbo2SQ8AkIJJDwCQwnxWSUspC4CWoq+gHKGslY2kBwBIYW6d8ESfiQNAKdKdtiQ9AEAKJj0AQAqPlLceLmkpZQGQkbJWDJIeACCF3UnPbVoj4QGAuOnOSKsplyDpAQBSMOkBAFLYU97atQCPkhYAGUUoa7FO0gMApDDvTW48UwuAW5nPC6NUNb5O0vAs6QEAUjDpAQBSuFfeWkaL+lrFsNHHBYDHv8+zNS8/vf3t+d/nd5duSHoAgBTm0qsvtxZ1O9e2K3r6kzUVK73fpfanxAroI+5b62O+9eeVerzX/ZP0AAApmPQAACnsfuBopMivdaxdavsjRKaRxrLHUiCQU7YG5t5JegCAvEnPNE1xLvsDJhG963EsI6ViR8a7x+3Pum8jHrPeo/3cnj4WSQ8AkIJJDwCQwhy9DBJhG0YoEYwyjr2XU3ou02Xet1ZKH7evvZ737T5lrf5JegCAdElPmChglFQigpHHUrLAiFods0dS1CPHYNTvKN8rY5L0AAApmPQAALnKW488XLR0/Fcz5nxk22tsn5JNjubmHrd5q5H37UyRyjw1v4dqPET2yH5oXh6LpAcASKHIs7eiK3W1UuOKpISI21SLpIyeRD9We0/tJDzlPb397dIzSQ8AkIJJDwCQwjxyvFuzCe/MlVN7jJXZbuSS3Mj7BvRH0gMApNA86Smt1RXlI7f8j9wUeVYCNnJS1uM2975vrbYl0rG6VYbUTvNyuObl2wOlyAdP0gMApGDSAwCkKW/1l7PS3NaI+97v9RjzA2Pppaz117ufhtqfPaXUUucKSQ8AkMK8t+E0ahNb1O0aTelxbt3wHNXITaMj71sGUZvS9+o9DanhqfPVl9dIegCAFEx6AIAUhlunh75Xtj5zdeueo3jOUeKztvVzpYTL2Q3MI5um6dMBtCzLoS9ySQ8AkMKc4Qqrtprb1fuzy177u66Mxx6DkfetFanTOA3M0p3LKU3zkh4AIAWTHgAgBY3MAJ3bG/1HeEDyWaK2PWylrLWtofnRpmZJDwCQgqQHILHek5GRmpczrsI8bbxxZW3pkUduY5f0AAApmPQAACkobxE26i7dbDnKgxKB/1s7pnspa0VoXn7q5OGia9/jnzU3P/947f+X9AAAKUh6CJuGjHYrLVBWz+lOy4TnKWCq88j5Zu0ccfM6q7e2S3oAgBRMegCAFLoub0UqxQBQR89lrRolrYjlq1pr/Ly2ns9Hkh4AIIWukx6IJsszjUbZNwlxP3pOd6Lclp7JS5UgSQ8AkIJJDwCQgvIWL1prCKv5d3u39UF6PRp534glUlnrSIPw/K7opvBg6V3SAwCksDvpcZv4faWvfluPc433XGIAbVLZI8de6++mM2W57TsbSQ8AkIJJDwCQwjxKI2SrpttsSo9zhrLWiOvbZNg3YqnRvKykNT5JDwCQglvWg4qeWN27qndLM8S96cBxWT/h+fD7m8uoPhzYt/nb95eaJD0AQAomPQBArvLWKA2JrdYR6nnMzmA88pX9Rt63Emp/x3ofjvnym19f/Nnff3xXdVsoR9IDAKQwL8vy6fJjmqYmlwWjJEwA9MPt6TlJegCAFEx6AIAU5pFXQa6xfa1LcsqD20X6nI78vvW0b60eDqzpG9qQ9AAAuZKetVu9a1+FnPV3t64eXOr1iCVSwgO96/14Kt3AfL213W3sfZD0AAApmPQAAOkamW8zy1T1G+UqWhq5qXXkfcvQ9N17KQs+J+kBAPLesr52q3fNq5C1q4uIV0HRuKru+wo1+lX/ESPv24jHb4/HD2wh6QEAUjDpAQBSr8h8zTY35axra/yUliUeLzF+WcZqjVie3tUo7ztO7rPuzpgkPQBACq8+eyvCKs1rIm1LdCM3hY98tTryZ3zkfTvLyJ91qEnSAwCkYNIDAKQwbY2Yp2n69Is7fv/SQk+RecTIOvr4RRwzoKwaN8dE9eH3N5cezN++v0S0dg67/QxJegCAFF5tZI60SvNW2a4KRml89r4Ba0p8//h+Gduy4zMi6QEAUjDpAQBS2FzeirhKM3V4/wAY4bwl6QEAUtiT9Dy8supaEzQArHGuoGRj+7Iszx8oSQ8AkIJJDwCQwnwkJrqu0rx17Z57KyUCALktB9Zmutd2I+kBAFI41Mh8TX2uic+Dr3FkEwCgCpWJ8zwyF7jzBIHVN0vSAwCkYNIDAKRwqLxVevVlpS4AorLmXHlbz/uPlLLWSHoAgBSmAOnKf1M1s2cAArl3jnTeqp7uHBpwSQ8AkIJJDwCQQpFG5oOeo6oApTYA+GjXEwco54yy1pWkBwBIIULSAwDRXJMF8U7n6c4tSQ8AkIJJDwCQgvIWAHC6rY3gZ5S1riQ9AEAKkh4A4BTRbvOX9AAAKZj0AAApKG8BAE1KWLUf2CrpAQBSkPQAwCCNuj2YKq2+vEbSAwCkYNIDAKSgvAUAO8oySlr9lbWuJD0AQAqTGSsA3DdNkxNmAbXTnVuSHgAgBZMeAOCSwT+EFmpN1//1MQAAAABJRU5ErkJggg=="
blcn64_string  = "iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABkUlEQVRYhWP8//8/A6lg0SMGojTFyTEwkmo2E8MgA0wMgwwwEoqyosuQ6DHgx5RjPjgfQ+yvfSJF0Tg0QqgIGirI4OvkFAZ0YF0zh+xQwxVSgy6EmBgGc5RZHYRElYUQcZoNsCR0cgBy9A26EGLBJni5yAXO1u3bgyEfIwuhlzxmwCkHAlc+MeBM9LiKh0EXQkwMgwywMK5HlDmWWBLziXcQmtiEjgwufMQUMyZQWQ++EGJAAr8LdcD01/4rOEMKPeGSCs4aQBKzMVKJjpzAB10IMTEM5ig7c/4qmLYkUnMMBVF36PBRONt6MEcZI8M6zPaHSTMkcYMAK5YEjg9M0UewsZXksGYMdy5m02VQhhATwyADLP8DEVU/rNSGJW4weIe7FCcH3Lv/AEzrIon16Q7i5gcjcgMNuV7DByxJDC1C9eCgDiEmhqHQDWLEFnVBiF6LiaE2zjKKuwXR2oSBrzV7MKIPOZqGXgghA0Y8CR25RCe2ZD9mP8S60kwMQy3KSI1G5DKKUPQMiRBiGmgHoAMAh9h4RuZlkGAAAAAASUVORK5CYII="
blcn64diff_string  = "iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABkUlEQVRYhWP8//8/A6lg0SMGojTFyTEwkmo2E8MgA0wMgwwwEoqyosuQ6DHgx5RjPjgfQ+yvfSJF0Tg0QqgIGirI4OvkFAZ0YF0zh+xQwxVSgy6EmBgGc5RZHYRElYUQcZoNsCR0cgBy9A26EGLBJni5yAXO1u3bgyEfIwuhlzxmwCkHAlc+MeBM9LiKh0EXQkwMgwywMK5HlDmWWBLziXcQmtiEjgwufMQUMyZQWQ++EGJAAr8LdcD01/4rOEMKPeGSCs4aQBKzMVKJjpzAB10IMTEM5ig7c/4qmLYkUnMMBVF36PBRONt6MEcZI8M6zPaHSTMkcYMAK5YEjg9M0UewsZXksGYMdy5m02VQhhATwyADLP8DEVU/rNSGJW4weIe7FCcH3Lv/AEzrIon16Q7i5gcjcgMNuV7DByxJDC1C9eCgDiEmhqHQDWLEFnVBiF6LiaE2zjKKuwXR2oSBrzV7MKIPOZqGXgghA0Y8CR25RCe2ZD9mP8S60kwMQy3KSI1G5DKKUPQMiRBiGmgHoAMAh9h4RuZlkGAAAAAASUVORK5CYII="

orcn64_string = "iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABtUlEQVRYhWP8//8/A6ng761mojQxq9Uykmo2E8MgA0wMgwwwEoqydwf8cSrY/jgAQyzC/AlF0Tg0QugdllCpXCaKoa496jWczS9lAqZXnJQhKtRwhdSgCyEmhsEcZW+3qGNEFSOPBkkGwqKOFIAcfYMuhFiwCUZMlIWzV+TfwJBn1agF03+erMaQ+8qkCGfD5JFDDZbocRUPgy6EmBgGGWC5u1gYS0mMiDJqgI/PziDxZPBW1oMvhBiQQES/JJheUXgeSVQEp+b/XzATPCHgKbsBYsdJRD2InMAHXQgxMQzmKDtz/iqUJUSUZlZoeUQOOHT4KJwdYS4/eEOI8c4iIYxsD0vcILCj6TcDKQA51H7faMaQr9pki9F0QQaDLoSYGAYZYFGOfQuv+mGlNiJxMzB8eI+ZwAUEcZdNhMC9+w+gLG64mJDDRsah0UC7i7VeIw7AQu3D+zcYYtgAsjrkWBp0IcTEMBS6QXexRJ1K3Ds428RQG0yvKHyOoTdjkSGG2Ir8xxhiwj43GYdHV/ounoSOXKLDALZQQwbICXhIhBATw1CLMmyA2PKKUPQMiRBiGmgHoAMAPbiPk2ZNHtIAAAAASUVORK5CYII="
root.geometry("1480x740")

canvas = tk.Canvas(root, width=1480, height=740, bg="lightblue", highlightthickness=0)
canvas.pack(fill="both", expand=True)

c4_board = tk.PhotoImage(data=board64_string)
c4_logo = tk.PhotoImage(data=logo64_string)
c4_blue_chip = tk.PhotoImage(data=blcn64_string)
c4_orange_chip = tk.PhotoImage(data=orcn64_string)

logo =canvas.create_image(740, 100, image=c4_logo, anchor="center")
board = canvas.create_image(740, 500, image=c4_board, anchor="center")
orange_chip = canvas.create_image(1110, 500, image=c4_orange_chip, anchor="center")
blue_chip = canvas.create_image(370, 500, image=c4_blue_chip, anchor="center")

diff_blue_chip = tk.PhotoImage(data=blcn64diff_string)
my_image = canvas.create_image(500, 500, image=diff_blue_chip, anchor="center")

def move(e):
    global diff_blue_chip
    diff_blue_chip = tk.PhotoImage(data=blcn64diff_string)
    my_image = canvas.create_image(e.x, e.y, image=diff_blue_chip, anchor="center")
    coordinate_label.config(text="Coordinates: x "+str(e.x) + "y" + str(e.y))



coordinate_label = tk.Label(root,text="")
coordinate_label.pack(pady=20)

canvas.bind('<B1-Motion>', move)
root.mainloop()














# MAIN CODE FOR THE GAME #
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
                self.grid_clear()
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
            
            return self.vertical_check(node, count, color) or self.horizontal_check(column, node_height, color) or self.right_diagonal_check(column, node_height, color) or self.left_diagonal_check(column,node_height, color)
        pass

# lst = LinkedList()
# lst.append(Node(27722))
# lst.append(Node("sksks"))
# lst.append(Node(82827))
# print(lst)
# lst.clear()
# print(lst)

#GAME_1 = Connect4()
#print(GAME_1)
# GAME_1.play(2, "Blue")
# GAME_1.play(3, "Blue")
# GAME_1.play(1, "Yellow")
# GAME_1.play(4, "Yellow")
# GAME_1.play(1, "Yellow")
# GAME_1.play(4, "Yellow")
# GAME_1.play(2, "Yellow")
# GAME_1.play(3, "Yellow")



# GAME_1.play(1, "Orange")
# GAME_1.play(2, "Blue")
# GAME_1.play(2, "Orange")
# GAME_1.play(3, "Blue")
# GAME_1.play(3, "Blue")
# GAME_1.play(3, "Orange")
# GAME_1.play(4, "Blue")
# GAME_1.play(4, "Blue")
# GAME_1.play(4, "Blue")
# GAME_1.play(4, "Orange")
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



