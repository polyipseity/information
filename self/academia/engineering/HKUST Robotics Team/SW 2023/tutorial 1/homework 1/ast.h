#include <stdint.h>

extern int const priorities[6];
typedef enum op_t
{
	PLUS,
	MINUS,
	MULTIPLY,
	DIVIDE,
	POWER,
	PARENTHESIS,
} op_t;
op_t op_from_char(char chr);
char op_to_char(op_t op);

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
