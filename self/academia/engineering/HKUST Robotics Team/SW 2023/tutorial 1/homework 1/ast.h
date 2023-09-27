#pragma once
#include <stdint.h>

typedef enum op_t
{
	INVALID = -1,
	PLUS,
	MINUS,
	MULTIPLY,
	DIVIDE,
	POWER,
	PARENTHESIS,
	END,
} op_t;
op_t op_from_char(char chr);

typedef double(op_function)(double, double);
extern int const op_priorities[END - PLUS + 1];
extern op_function *const op_functions[END - PLUS + 1];

typedef struct ast_t
{
	enum
	{
		OPERATOR,
		VALUE
	} tag;
	union
	{
		intmax_t val;
		op_t op;
	};
} ast_t;
ast_t ast_from_op(op_t op);
ast_t ast_from_val(intmax_t val);
