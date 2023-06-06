#include "lists.h"

/**
 * insert_node - Insert node
 * @head: head pointer
 * @number: number
 * Return: NULL / New node
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = *head;
listint_t *newNode = malloc(sizeof(listint_t));
if (newNode == NULL)
{
return (NULL);
}
newNode->data = number;

if (current == NULL || current->data >= number)
{
newNode->next = current;
*head = newNode;
return (newNode);
}

while (current && current->next && current->next->data < number)
{
	current = current->next;
}

newNode->next = current->next;
current->next = newNode;

return (newNode);
}

