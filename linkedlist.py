class Node():
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None    
        self.size = 0

    def get_size(self) -> int:
        return self.size
    
    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next 
        return   

    def append_to_list(self, data: int) -> None:
        # Adding first element to the LL:
        self.size += 1
        if self.head is None:
            self.head = Node(data)
            return None
        
        # Adding elements to the LL:
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = Node(data)
        return None

    def insert_at_index(self, data: int, index: int) -> None:
        if index > self.size - 1:
            raise IndexError("Index out of range.")

        self.size += 1
        
        temp = self.head
        if index == 0:
            self.head = Node(data)
            if temp is not None:
                self.head.next = temp
            return None

        i = 0
        previous = None
        while i <= index:
            if i == index:
                previous.next = Node(data)
                previous.next.next = temp
                return None
            previous = temp
            temp = temp.next        
            i += 1

        return
        
    
    def delete_from_list(self, data: int) -> None:
        """
        Delete the first occurance of the data from the LL.
        If the data is not found, return None.
        """
        if self.head is None:
            print("The linked list is empty; nothing to delete.")
            return None
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return None
        
        temp = self.head
        previous = None
        while temp is not None:
            if temp.data == data:
                previous.next = temp.next
                self.size -= 1
                return None
            previous = temp
            temp = temp.next
        
        raise ValueError("Data not found in the linked list.")
    
    def pop(self, index: int | None = None) -> int:
        """
        Delete the last element from the LL, or from the passed in index position.
        """
        if index is None:
            index = self.size - 1

        if self.head is None:
            print("The linked list is empty; nothing to delete.")
            return None
        
        if index == 0:
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            return temp.data
        
        i = 0
        temp = self.head
        previous = None
        while temp is not None:
            if i == index:
                previous.next = temp.next
                self.size -= 1
                return temp.data
            previous = temp
            temp = temp.next
            i += 1
            
        raise IndexError("Index out of range.")

def main():
    # head: Node = Node(1)
    # print(head.data)
    # print(head.next)
    # n2: Node = Node(5)
    # head.next = n2
    # print(head.next.data)
    # print(head.next.next)
    # n3: Node = Node(10)
    # n2.next = n3
    # print(head.next.next.data)
    # print(n2.next.data)
    # ll: LinkedList = LinkedList()
    # ll.head = head
    # ll.print_list()
    ll: LinkedList = LinkedList()
    ll.append_to_list(1)
    ll.append_to_list(5)
    ll.append_to_list(10)
    # ll.print_list()
    # print(ll.pop())
    # print(ll.pop(0))
    # print(ll.pop(1))
    # ll.print_list()
    # ll.delete_from_list(5)
    ll.print_list()
    # ll.delete_from_list(15)
    ll.insert_at_index(15, 1)
    ll.print_list()

    return

if __name__ =="__main__":
    main()
