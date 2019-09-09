#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks for cycle in linked list
 * @list: pointer to head of linked list
 * Return: 1 if cycle, 0 if not cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
