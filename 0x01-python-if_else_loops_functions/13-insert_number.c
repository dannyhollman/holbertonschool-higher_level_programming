#include "lists.h"
/**
 * insert_node - inserts node into sorted linked list
 * @head: pointer to head of linked list
 * @number: value of new node
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new, *previous;

	new = malloc(sizeof(listint_t));
	temp = *head;
	previous = *head;
	new->n = number;

	while (temp)
	{
		if (temp->n > number)
		{
			previous->next = new;
			new->next = temp;
			return (new);
		}
		previous = temp;
		temp = temp->next;
	}
	return (*head);
}
