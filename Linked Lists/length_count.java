class LinkedList{
	Node head;

	class Node{
	int data;
	Node next;
	Node(int d)
		{
		data = d;
		next = null;
		}	
	}

	 public void push(int new_data)
	 {
	 	Node new_node = new Node(new_data);

	 	new_node.next = head;
	 	head  = new_node;

	 }

    public int count()
    {
    	Node h = head;
    	int count = 0;
    	while(h!=null)
    	{
    		count++;
    		h = h.next;
    	}
    	return count;
    }
    public static void main(String[] args)
    {
        /* Start with the empty list */
        LinkedList llist = new LinkedList();
        llist.push(1);
        llist.push(3);
        llist.push(1);
        llist.push(2);
        llist.push(1);
 
        System.out.println("Count of nodes is " +
                           llist.getCount());
    }

}