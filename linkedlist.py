class Node():
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None    

    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next 
        return   

    def append_to_list(self, data: int) -> Node:
        # Adding first element to the LL:
        if self.head is None:
            self.head = Node(data)
            return self.head
        
        # Adding elements to the LL:
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = Node(data)
        return self.head

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
    ll.print_list()
    return

if __name__ =="__main__":
    main()
