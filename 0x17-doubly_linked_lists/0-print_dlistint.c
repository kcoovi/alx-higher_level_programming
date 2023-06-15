#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - function
 * @h: pointer
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t c;

	c = 0;

	while (h)
	{
	printf("%d\n", h->n);
	h = h->next;
	count++;
	}

	return (c);
}
