#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include "str.h"

str_t *str_malloc(size_t len)
{
	str_t *self = malloc(sizeof(str_t) + (len + 1) * sizeof(char));
	self->len = len;
	self->data[len] = '\0';
	return self;
}

str_t *str_calloc(size_t len)
{
	str_t *self = str_malloc(len);
	memset(self->data, '\0', len * sizeof(char));
	return self;
}

void str_realloc(str_t **const self, size_t len)
{
	*self = realloc(*self, sizeof(str_t) + (len + 1) * sizeof(char));
	(*self)->len = len;
	(*self)->data[len] = '\0';
}

void str_recalloc(str_t **const self, size_t len)
{
	size_t old_len = (*self)->len;
	str_realloc(self, len);
	if (len > old_len)
	{
		memset(&(*self)->data[old_len], '\0', (len - old_len) * sizeof(char));
	}
}

void str_free(str_t *const self)
{
	free(self);
}
