#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>


/**
 * struct ListNode - Structure representing a node in a singly linked list
 * @data: The data stored in the node
 * @next: A pointer to the next node in the list
 *
 * Description: This structure defines a node in a singly linked list.
 * It contains an integer data element and a pointer to the next node
 */

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif /* LISTS_H */
