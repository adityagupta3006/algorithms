class appendL{
	Node head;

	class Node{
		int data;
		Node next;
		Node(int d){
			data = d;
			next = null;
		}
	}
	public void push(int new_data){
		Node new_node = new Node(new_data);
		new_node.next = head; 
		head = new_node;
	}

	public void insertAfter(Node prevNode, int new_data){
		if (prevNode==null){
			System.out.println("error");
			return;
		}
		Node new_node = new Node(new_data);
		new_node.next = prevNode.next;
		prevNode.next = new_node;
	}

	public void append(int new_data){
		Node new_node = new Node(new_data);
		if (head == null){
			head = new_node;
			return;
		}
		new_node.next = null;
		Node n = head;
		while (n!=null){
			n = n.next; 
		}
		n.next = new_node;
		return;
	}
	public void printList(){
		Node head_node = head;
		while (head_node!=null){
			System.out.println(head_node.data + " ");
			head_node = head_node.next;
		}
	}

    public static void main(String[] args)
    {
        /* Start with the empty list */
        appendL llist = new appendL();
 
        // Insert 6.  So linked list becomes 6->NUllist
        llist.append(6);
 
        // Insert 7 at the beginning. So linked list becomes
        // 7->6->NUllist
        llist.push(7);
 
        // Insert 1 at the beginning. So linked list becomes
        // 1->7->6->NUllist
        llist.push(1);
 
        // Insert 4 at the end. So linked list becomes
        // 1->7->6->4->NUllist
        llist.append(4);
 
        // Insert 8, after 7. So linked list becomes
        // 1->7->8->6->4->NUllist
        llist.insertAfter(llist.head.next, 8);
 
        System.out.println("\nCreated Linked list is: ");
        llist.printList();
    }
}