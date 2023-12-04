#include "lists.h"

/**
 * rev_listnode - reverses a list
 * @head: contains the address of the first node
 */
void rev_listnode(listint_t **head)
{
	listint_t *prv = NULL;
	listint_t *crt = *head;
	listint_t *next = NULL;

	while (crt != NULL)
	{
		next = crt->next;
		crt->next = prv;
		prv = crt;
		crt = next;
	}
	*head = prv;
}

/**
 * is_palindrome - checks whether a linked list is a palindrome
 * @head: contains the address of the node
 * Return: 0 if false else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *tort = *head, *hare = *head;
	listint_t *onehalf = *head, *twohalf = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		hare = hare->next->next;
		if (!hare)
		{
			twohalf = tort->next;
			break;
		}
		if (!hare->next)
		{
			twohalf = tort->next->next;
			break;
		}
		tort = tort->next;
	}
	rev_listnode(&twohalf);
	while (twohalf && onehalf)
	{
		if (onehalf->n == twohalf->n)
		{
			twohalf = twohalf->next;
			onehalf = onehalf->next;
		}
		else
			return (0);
	}
		if (twohalf == NULL)
			return (1);
		return (0);

}
