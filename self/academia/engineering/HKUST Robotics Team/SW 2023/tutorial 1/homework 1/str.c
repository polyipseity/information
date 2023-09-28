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
	str_t *ret = realloc(*self, sizeof(str_t) + (len + 1) * sizeof(char));
	ret->len = len;
	ret->data[len] = '\0';
	*self = ret;
}

void str_recalloc(str_t **const self, size_t len)
{
	str_t *ret = *self;
	size_t old_len = ret->len;
	str_realloc(&ret, len);
	if (len > old_len)
	{
		memset(&ret->data[old_len], '\0', (len - old_len) * sizeof(char));
	}
	*self = ret;
}

void str_free(str_t *const self)
{
	free(self);
}
