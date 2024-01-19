#include "lists.h"

int helper(listint_t **head, listint_t *curr);

/**
 * is_palindrome - check if linked list is palindrome
 * @head: head of the linked list
 * Return: 1 if linked list is palindrome or 1 if it's not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;

	if (!head || !head->next)
		return (1);

	fast = slow = head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast)
		slow = slow->next;

	return (helper(head, slow));
}

/**
 * helper - helper of is_palindrome function
 * @start: pointer to the linked list node
 * @end: pointer to the linked list node
 * Return: 1 if linked list is palindrome or 1 if it's not
 */
int helper(listint_t **start, listint_t *end)
{
	int is_palindrome, val;

	if (!end)
		return (1);

	is_palindrome = helper(start, end->next);

	val = (*start)->val;
	*start = (*start)->next;

	if (val == end->val && is_palindrome)
		return (1);

	return (0);
}
