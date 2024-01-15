#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if there is a cycle in list
 * @list: head of the list
 * Return: 1 if there is a cycle or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
