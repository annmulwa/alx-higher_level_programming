#include "lists.h"

/**
 * check_cycle - checks if a linked list is a cycle
 * @list: linked list
 * Return: 1 if it is a cycle else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *tort, *rab;

	if (list == NULL || list->next == NULL)
		return (0);
	tort = list;
	rab = list;

	while(tort != NULL && rab != NULL && rab->next != NULL)
	{
		tort = tort->next;
		rab = rab->next->next;
		if (rab == tort)
		{
			return (1);
		}
	}
	return (0);
}
