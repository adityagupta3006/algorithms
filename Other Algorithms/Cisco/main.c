#include<stdio.h>
#include<stdlib.h>
#define SIZE 26    // Alphabets of a letter

void add(char *name, char *phonenumber);
void print(char *name);

/*Structure of 
 a contact.
*/
struct Node
{
    struct Node* next;
    char* user;
    char* number;
};

struct Node *phonebook[26]; // making 26 nodes for each alphabet

// add function takes name and phone number as input

void add(char *name, char *phonenumber)
{
    /* Hash function coverts the ascii and stores
    *  computes where the contact needs to be stored.
    */    
    int index=(int)((name[0]-65)%26); 
    
    struct Node *contact=(struct Node*) malloc (sizeof(struct Node));
    contact->next=NULL; // pointing nexr to null
    contact->user=name; // storing contact name
    contact->number=phonenumber; // storing contact phone number
    

    // check if the head is null
    // and add head 
    if(phonebook[index] == NULL)
    {
        phonebook[index]=contact;
    }
    // make new entry as head and 
    // point next of new entry to head
    else
    {    
        contact->next=phonebook[index]; // Adding at head. Handling the collisions
        phonebook[index]=contact;       // updating head.
    }    
        
}
// printing the contact
void print(char *name)
{
    int index=(int)((name[0]-65)%26); 
    struct Node *traverse=phonebook[index];
    
    /* traverse through the contact list
    *  until we reach the end or we find the contact
    */
    while(traverse!=NULL && traverse->user!=name)
    {
        traverse=traverse->next;
    }
    // If we have found the contact 
    if(traverse!=NULL)
    {
        printf("Name is %s\n", traverse->user);
        printf("Number is %s\n",traverse->number);
    }
    // if the entry is not present in the directory.
    else
    {
        printf("Entry not found");
    }
    
}

int main()
{
    add("Aditya","9803371707");
    add("Vishal","9803371708");
    add("Deepanjan","9803371709");
    add("Alok","9803371706");
    print("Aditya");
}