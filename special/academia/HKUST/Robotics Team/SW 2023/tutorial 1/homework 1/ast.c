#include "ast.h"

op_t op_from_char(char chr)
{
	switch (chr)
	{
	case '+':
		return PLUS;
	case '-':
		return MINUS;
	case '*':
		return MULTIPLY;
	case '/':
		return DIVIDE;
	case '(':
		return PARENTHESIS;
	default:
		return INVALID;
	}
}

intmax_t plus(intmax_t a, intmax_t b)
{
	return a + b;
}
intmax_t minus(intmax_t a, intmax_t b)
{
	return a - b;
}
intmax_t multiply(intmax_t a, intmax_t b)
{
	return a * b;
}
intmax_t divide(intmax_t a, intmax_t b)
{
	return a / b;
}
int const op_priorities[] = {0, 0, 1, 1, -1};
op_function *const op_functions[] = {&plus, &minus, &multiply, &divide};

ast_t ast_from_op(op_t op)
{
	ast_t self = {.tag = OPERATOR, .op = op};
	return self;
}

ast_t ast_from_val(intmax_t val)
{
	ast_t self = {.tag = VALUE, .val = val};
	return self;
}
