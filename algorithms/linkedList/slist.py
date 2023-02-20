class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None
        def __str__(self):
            return f"{self.value}"

    def __init__ (self):
        self._head = None
        self._tail = None
        self._size = 0

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        def prepend(self, new_node):
            new_node.next = self._head
            self._head = new_node
                
        def insertAfterPos(self, current_node, new_node):
            if current_node is self._tail:
                self._tail.next = new_node
                self._tail = new_node
            else:
                new_node.next = current_node.next
                current_node.next = new_node
  
        def findInsertionPos(self, value):
            currNodeA = None
            currNodeB = self._head
            while (currNodeB != None and value >= currNodeB.value):
                currNodeA = currNodeB
                currNodeB = currNodeB.next
            return currNodeA

        newNode = self.SListNode(value)
        if self._head == None: # if list empty, add node
            self._head = newNode
            self._tail = newNode
            self._size += 1
        else: # if list not empty, begin search for appropriate spot in the list for insertion
            insertionPos = findInsertionPos(self, newNode.value)
            #if FindinsertionPos() returns None: prepend to head
            if insertionPos == None:
                prepend(self, newNode)
                self._size += 1
            #if FindInsertionPos() returns node, insert after node
            else:
                insertAfterPos(self, insertionPos, newNode)
                self._size += 1
    
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        node = self._head
        while node != None:
            if node.value == value:
                return node.value
            node = node.next
        return None

    '''Remove the first occurance of value.'''
    def remove(self, value):
        def remove_after(self, current_node):
            if current_node.next != None:
                succeeding_node = current_node.next.next
                current_node.next = succeeding_node
                if succeeding_node == None: # Remove tail
                    self._tail = current_node
        
        node = self._head
        #check head for match
        if node.value == value:
            succeeding_node = self._head.next
            self._head = succeeding_node
            self._size -= 1
            return True
            #proceed through list until match
        for _ in range(self._size):
            if node.next != None: 
                if node.next.value == value:
                    remove_after(self, node)
                    self._size -= 1
                    return True
            node = node.next
        #no match found: return false
        return False

    '''Remove all instances of value'''
    #Counts the number of occurrences and then calls self.remove amount times
    def remove_all(self, value):
        amount = 0
        node = self._head
        for _ in range(self._size):
            if node.value == value:
                amount += 1
            node = node.next
        for _ in range(amount):
            self.remove(value)

    '''Convert the list to a string and return it'''
    def __str__(self):
        if self._size == 0:
            return "[]"
        else:
            node = self._head
            myStr = "["
            while node != None:
                myStr += str(node.value) + ", "
                node = node.next
            myStr = myStr[0:-2] #deletes ', ' on last int
            return myStr + ']'

    '''Return an iterator for the list'''
    def __iter__(self):
        item = self._head
        while item is not None:
            yield item
            item = item.next

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        if index >= self._size:
            raise IndexError("Invalid Index")
        else:
            item = self._head
            for _ in range(index):
                item = item.next
            return item

    def __len__(self):
        return self._size
    