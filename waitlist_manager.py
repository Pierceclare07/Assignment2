# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None   
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
class Linkedlist:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node 
        print(f"{name} added to the front of the waitlist")

    def add_end(self, Name):
        new_node = Node(Name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"{Name} added to the end of the waitlist")

    def remove(self, name):
        if not self.head:
            print(f"{name} not found")
            return
        
        if self.head == name:
            self.head = self.head.next
            print(f"Removed {name} from the waitlist")
            return
        current = self.head
        while current.next and current.next.name != name:
            current = current.next
        if current.next:
            current.next = current.next.next
            print(f"Removed {name} from the waitlist")
        else:
            print(f"{name} not found")

    def print_list(self):
        if not self.head:
            print("The waitlist is empty")
            return
        
        print("Current waitlist:")
        current = self.head
        while current:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    waitlist = Linkedlist()
    
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
            

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
            

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)
            
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()
            
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

if __name__ == "__main__":
    waitlist_generator()


'''
This program manages a customer waitlist using a singly linked list. A linked list is a sequence of nodes, where each node stores a piece of data (in this case, the customer’s name) and a pointer to the next node. Instead of relying on Python’s built-in list type, this implementation creates a custom structure that highlights how dynamic lists can be managed in memory.
The list is controlled by a special reference called the head. The head points to the first node in the sequence and acts as the entry point into the entire waitlist. If the head is None, it means the waitlist is empty. When a new customer is added to the front, the head is updated to point to this new node, while the new node points to the previous head. When customers are added to the end, the program traverses the list from the head until it finds the last node, then links the new node there. Removing a customer involves carefully updating the next pointer of the previous node so that it skips the removed node.
In real-world engineering, custom linked lists are useful when data structures need to support frequent insertions and deletions without the overhead of shifting elements, as happens in arrays. Operating systems, for example, use linked lists to manage processes or memory blocks. Networking software may use them to queue data packets. This program demonstrates the core concepts behind such systems, showing how a simple custom list can be designed to manage dynamic, changing data efficiently.

'''
