/* node = root
 * while(node) - stack.push(node)
 * node= node->left
 *
 *              10
 *
 *          7
 *
  *      5      8
 *
 *  1       6
 *
 *  1 - 5 - 6 - 7 - 8 - 10 - 12 - 22 - 23 - 26
 *
 *  10
 *  6
 *
 * */

 struct node{
     int data;
     struct node left;
     struct node right;
 };

 // creating global
 int size = 0; // to maintain stack size
 stack<int> new_stack;

 int findKlowest(struct node *root_reference, int k)
 {
     node *new_node = root_reference;

     /* calling inorder function to populate the stack
      * with elements from lowest to highest.
      */
     int smallest_node = inOrder(new_node);
     return smallest_node;
 }

 int inOrder(struct node *node_ref){

     /*when the size of stack becomes equal to k
      * return the top element of stack
      *
      * example - tree size = 100000
      * required - 6th smallest element
      * After pushing 6 elements in the stack
      * we can check the size of stack and return
      * the top element
      * */
     if(size == k) {
         int x = new_stack.pop();
         return x;
     }

     if(node_ref == NULL)
     {
         return;
     }
     inOrder(node->left);
     new_stack.push(node->data);
     size++;
     inOrder(node->right);
 }
