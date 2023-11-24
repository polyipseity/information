#pragma once
#include <string.h>

typedef struct str_t
{
	size_t len;
	char data[];
} str_t;
str_t *str_malloc(size_t len);
str_t *str_calloc(size_t len);
void str_realloc(str_t **restrict self, size_t len);
void str_recalloc(str_t **restrict self, size_t len);
void str_free(str_t *restrict self);
