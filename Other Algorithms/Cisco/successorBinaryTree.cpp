/*
 *  Author - Aditya Gupta
 *  
 *
 *
 * */

 bool inorder(struct node *node) {
    if(!node->right)
        return false;

    if(node->left){
        cout << node->left->data;
        return true;
    }
    else{
        cout << node->right->data;
    }
 }
// node->right
 int inorderMin(struct node *node){
    while(node){
        if(!node->left){
                break;
        }
        node = node->left;
    }
    return node->data;
 }