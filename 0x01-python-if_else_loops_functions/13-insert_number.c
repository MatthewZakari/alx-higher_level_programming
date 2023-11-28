#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of the head of the list
 * @number: value to insert into the list
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_node, *crent, *prev;

	n_node = malloc(sizeof(listint_t));
	if (n_node == NULL)
		return (NULL);

	n_node->n = number;
	n_node->next = NULL;

	crent = *head;
	prev = NULL;

	while (crent != NULL && crent->n < number)
	{
		prev = crent;
		crent = crent->next;
	}

	if (prev == NULL)
	{
		n_node->next = *head;
		*head = n_node;
	}
	else
	{
		n_node->next = crent;
		prev->next = n_node;
	}

	return (n_node);
}
