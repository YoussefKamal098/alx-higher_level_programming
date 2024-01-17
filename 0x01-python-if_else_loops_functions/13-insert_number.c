#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in sorted list
 * @head: head of the list
 * @number: number of the node
 * Return: inserted node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *node;

	if (!head)
		return (NULL);

	node = (listint_t *)malloc(sizeof(listint_t));

	if (!node)
		return (NULL);

	node->n = number;

	while (curr)
	{
		if (!curr->next || number > curr->n)
		{
			node->next = curr->next;
			curr->next = node;
			return (node);
		}

		curr = curr->next;
	}

	return (NULL);
}
