typedef struct l_stack_t
{
	struct l_stack_t *prev;
	void *data;
} l_stack_t;
l_stack_t *l_stack_push(l_stack_t *self, void *data);
l_stack_t *l_stack_pop(l_stack_t *self, void **data);
l_stack_t *l_stack_reverse(l_stack_t *self);
void l_stack_free(l_stack_t *self, void (*freer)(void *));
