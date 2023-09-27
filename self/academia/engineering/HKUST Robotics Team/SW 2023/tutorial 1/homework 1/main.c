#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include "ast_t.h"
#include "l_stack_t.h"
#include "str_t.h"

char const *const msg_cannot_input = "Please input a math equation:\n";
char const *const msg_cannot_output = "Output:\n";
char const *const error_msg = "ERROR! The string input is not supported!!\n";

void read_line(str_t *ret, FILE *stream)
{
    for (char cc = getc(stream); cc != EOF && cc != '\n'; cc = getc(stream))
    {
        size_t idx = ret->len;
        ret = str_t_realloc(ret, idx + 1);
        ret->data[idx] = cc;
    }
}

bool parse(ast_t **ret, str_t *input)
{
    *ret = NULL;
    intmax_t val = 0;
    for (size_t ii = 0; ii < input->len; ++ii)
    {
        char chr = ret->data[ii];
        switch (chr)
        {
        case '0':
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            val *= 10;
            val += chr - '0';
            break;
        case '+':
        case '-':
        case '*':
        case '/':
            break;
        case '(':
            break;
        case ')':
            break;
        default:
            return true;
        }
    }
    return false;
}

int main(void)
{
    str_t *input = str_t_malloc(0);
    read_line(input, stdin);
    str_t *ast_t = str_t_malloc(0);
    parse(ast_t, input);
    str_t_free(ast_t);
    str_t_free(input);
    return 0;
}
