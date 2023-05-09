#include "lists.h"

/**
 * check_cycle - checks if a linked list has a loop
 * @list: pointer to head of list
 *
 * Return: 0 || 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);

	fast = list->next;
	slow = list;

	while (fast && fast->next && slow)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}

	return (0);
}
