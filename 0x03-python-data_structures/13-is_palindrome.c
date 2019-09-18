#include "lists.h"
/**
 * is_palindrome - checks if linked list is palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int len = 0, start = 0;
	listint_t *temp = *head;
	int numbers[100];

	if (!(*head))
		return (1);
	while (temp)
	{
		numbers[len] = temp->n;
		len++;
		temp = temp->next;
	}
	len--;
	if (len % 2 == 0)
	{
		while (start < len)
		{
			if (numbers[start] != numbers[len])
				return (0);
			start++;
			len--;
		}
		return (1);
	}
	if (len % 2 != 0)
	{
		while (start < (len / 2))
		{
			if (numbers[start] != numbers[len])
				return (0);
			start++;
			len--;
		}
		return (1);
	}
	return (0);
}
