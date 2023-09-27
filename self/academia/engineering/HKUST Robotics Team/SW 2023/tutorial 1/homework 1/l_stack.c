#include <stdlib.h>
#include "l_stack.h"

void l_stack_push(l_stack_t **const self, void *data)
{
	l_stack_t *ret = malloc(sizeof(l_stack_t));
	ret->prev = *self;
	ret->data = data;
	*self = ret;
}

void *l_stack_pop(l_stack_t **const self)
{
	l_stack_t *next = *self;
	void *data = next->data;
	*self = next->prev;
	free(next);
	return data;
}

void l_stack_reverse(l_stack_t **const self)
{
	l_stack_t *prev = NULL, *next;
	while (*self)
	{
		next = (*self)->prev;
		(*self)->prev = prev;
		prev = *self;
		*self = next;
	}
	*self = prev;
}

void l_stack_free(l_stack_t *self, void (*freer)(void *))
{
	if (freer)
	{
		while (self)
		{
			(*freer)(l_stack_pop(&self));
		}
	}
	else
	{
		while (self)
		{
			l_stack_pop(&self);
		}
	}
}
