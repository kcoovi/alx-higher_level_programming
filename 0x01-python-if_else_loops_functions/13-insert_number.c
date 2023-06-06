#include "lists.h"
/**
 * insert_node - insert node
 * @head: head
 * @number: number
 * Return: NULL / New node
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head;
listint_t *new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->data = number;

	if (node == NULL || node->data >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	while (node->next && node->next->data < number)
	{
		node = node->next;
	}

	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}
