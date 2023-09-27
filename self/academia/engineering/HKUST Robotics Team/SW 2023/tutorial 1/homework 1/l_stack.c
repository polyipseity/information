#include <stdlib.h>
#include "l_stack.h"

l_stack_t *l_stack_push(l_stack_t *self, void *data)
{
	l_stack_t *ret = malloc(sizeof(l_stack_t));
	ret->prev = self;
	ret->data = data;
	return ret;
}

l_stack_t *l_stack_pop(l_stack_t *self, void **data)
{
	l_stack_t *prev = self->prev;
	*data = self->data;
	free(self);
	return prev;
}

l_stack_t *l_stack_reverse(l_stack_t *self)
{
	l_stack_t *prev = NULL, *next;
	while (self)
	{
		next = self->prev;
		self->prev = prev;
		prev = self;
		self = next;
	}
	return prev;
}

void l_stack_free(l_stack_t *self, void (*freer)(void *))
{
	void *val;
	while (self)
	{
		self = l_stack_pop(self, &val);
		if (freer)
		{
			(*freer)(val);
		}
	}
}
