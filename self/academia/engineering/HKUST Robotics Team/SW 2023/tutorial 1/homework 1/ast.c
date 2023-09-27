#include "ast.h"

int const priorities[] = {0, 0, 1, 1, 2, -1};

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
	case '^':
		return POWER;
	case '(':
		return PARENTHESIS;
	default:
		return -1;
	}
}

char op_to_char(op_t op)
{
	switch (op)
	{
	case PLUS:
		return '+';
	case MINUS:
		return '-';
	case MULTIPLY:
		return '*';
	case DIVIDE:
		return '/';
	case POWER:
		return '^';
	case PARENTHESIS:
		return '(';
	default:
		return '\0';
	}
}

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
