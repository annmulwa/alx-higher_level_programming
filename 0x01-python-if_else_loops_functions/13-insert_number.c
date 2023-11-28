#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * insert_node - inserts a number in a linked list
 * @head: contains the address of the node
 * @number: number to be inserted
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *crt = *head;
	listint_t *newn = NULL;
	listint_t *tmp = NULL;

	if (head == NULL)
		return (NULL);
	newn = malloc(sizeof(listint_t));
	if (newn == NULL)
		return (NULL);
	newn->n = number;
	newn->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		newn->next = *head;
		return (*head = newn);
	}
	else
	{
		while (crt && crt->n < number)
		{
			tmp = crt;
			crt = crt->next;
		}
		tmp->next = newn;
		newn->next = crt;
	}
	return (newn);
}




