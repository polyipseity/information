#include <limits.h>
#include <stdbool.h>
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
	case '^':
		return POWER;
	case '(':
		return PARENTHESIS;
	default:
		return INVALID;
	}
}

double plus(double a, double b)
{
	return a + b;
}
double minus(double a, double b)
{
	return a - b;
}
double multiply(double a, double b)
{
	return a * b;
}
double divide(double a, double b)
{
	return a / b;
}
double exp(double a)
{
	double ret = 0;
	for (int ii = 0; ii < 1024; ++ii)
	{
		double term = 1;
		for (int jj = 1; jj <= ii; ++jj)
		{
			term *= a;
			term /= jj;
		}
		ret += term;
	}
	return ret;
}
double ln(double a)
{
	if (a == 0)
	{
		return 0 / 0;
	}
	bool negative = a < 0;
	if (negative)
	{
		a = -a;
	}
	int n = 0;
	while (a >= 10)
	{
		++n;
		a /= 10;
	}
	while (a < 1)
	{
		--n;
		a *= 10;
	}
	if (negative)
	{
		a = -a;
	}
	int y = (a - 1) / (a + 1);
	double ret = 0;
	for (int ii = 0; ii < 10; ++ii)
	{
		double term = 2.0 / (2 * ii + 1);
		for (int jj = 0; jj < 2 * ii + 1; ++jj)
		{
			term *= y;
		}
		ret += term;
	}
	return ret + 2.302585092994045684 * (n - 1);
}
double power(double a, double b)
{
	// f(x) = a^x
	// f(64) a^64
	// f'(64) = a^64 + 64a^63/1!(b-64) + 64*63*a^62/2!1(b-64)^2
	long long exp = b;
	double coefficient = 1;
	for (int ii = 0; ii < exp; ++ii)
	{
		coefficient *= a;
	}
	double term = 1, ret = coefficient * term;
	for (int terms = 1; terms <= exp; ++terms)
	{
		coefficient /= terms;
		coefficient /= a;
		coefficient *= exp - terms + 1;
		term *= b - exp;
		ret += coefficient * term;
	}
	return ret;
}
int const op_priorities[] = {0, 0, 1, 1, 2, -1, INT_MIN};
op_function *const op_functions[] = {&plus, &minus, &multiply, &divide, &power};

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
