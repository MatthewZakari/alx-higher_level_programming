#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;	/* Move one step */
		hare = hare->next->next;	/* Move two steps */

		if (tortoise == hare)
			return (1); /* There is a cycle */
	}

	return (0); /* No cycle */
}
