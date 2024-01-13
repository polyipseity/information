#include "l_stack.h"
#include "memory.h"

void l_stack_push(l_stack_t **restrict const self, void *restrict data)
{
	l_stack_t *restrict ret = malloc(sizeof(l_stack_t));
	ret->prev = *self;
	ret->data = data;
	*self = ret;
}

void *l_stack_pop(l_stack_t **restrict self)
{
	l_stack_t *restrict next = *self;
	void *restrict data = next->data;
	*self = next->prev;
	free(next);
	return data;
}

void l_stack_reverse(l_stack_t **restrict const self)
{
	l_stack_t *prev = NULL, *cur = *self, *next;
	while (cur)
	{
		next = cur->prev;
		cur->prev = prev;
		prev = cur;
		cur = next;
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
