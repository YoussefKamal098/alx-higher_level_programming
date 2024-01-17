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
	listint_t *curr, *new;

	if (!head)
		return (NULL);

	new = (listint_t *)malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	curr = *head;

	if (!curr || new->n < curr->n)
	{
		new->next = curr;
		return (*head = new);
	}

	while (curr)
	{
		if (!curr->next || new->n < curr->next->n)
		{
			new->next = curr->next;
			curr->next = new;
			return (new);
		}

		curr = curr->next;
	}

	return (NULL);
}
