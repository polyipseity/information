#pragma once
#include <string.h>

void *malloc(size_t size);
void *realloc(void *ptr, size_t new_size);
void free(void *ptr);
