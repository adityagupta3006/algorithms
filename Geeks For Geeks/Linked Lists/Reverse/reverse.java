class LinkedList{
	static Node head;
	
	static class Node{
		int data;
		Node next;

		Node (int d){
			data = d;
			next = null;
		}
	}

	Node reverse(Node node){

		Node prev = null;
		Node curr = node;
		Node next = null;

		while(curr!=null){
			next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = curr.next;
		}
		node = prev;
		return node;
	}

	void printList(Node node){
		while(node!=null){
			System.out.println(node.data + " ");
			node = node.next;
		}
	}
	public static void main(String[] args){
		LinkedList list = new LinkedList();
		list.head = new Node(85);
		list.head.next = new Node(15);
list.printList(head);
	}

}