#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include "ast.h"
#include "l_stack.h"
#include "str.h"

char const msg_input[] = "Please input a math equation:\n";
char const msg_output[] = "Output:\n";
char const error_msg[] = "ERROR! The string input is not supported!!\n";

str_t *read_line(FILE *restrict stream)
{
    str_t *ret = str_malloc(0);
    for (int cc = getc(stream); cc != EOF && cc != '\n'; cc = getc(stream))
    {
        size_t idx = ret->len;
        str_realloc(&ret, idx + 1);
        ret->data[idx] = cc;
    }
    return ret;
}

l_stack_t *parse_to_postfix(str_t const *restrict input)
{
    l_stack_t *ret = NULL, *op_stack = NULL;
    intmax_t val = -1;
    for (size_t ii = 0; ii < input->len; ++ii)
    {
        char chr = input->data[ii];
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
            if (val == -1)
            {
                val = 0;
            }
            val *= 10;
            val += chr - '0';
            break;
        default:
            if (val != -1)
            {
                ast_t *restrict ast = malloc(sizeof(ast_t));
                *ast = ast_from_val(val);
                l_stack_push(&ret, ast);
                val = -1;
            }
            op_t op = op_from_char(chr);
            if (op != INVALID)
            {
                if (op != PARENTHESIS)
                {
                    while (op_stack && op_priorities[((ast_t *)(op_stack->data))->op] >= op_priorities[op])
                    {
                        l_stack_push(&ret, l_stack_pop(&op_stack));
                    }
                }
                ast_t *restrict ast = malloc(sizeof(ast_t));
                *ast = ast_from_op(op);
                l_stack_push(&op_stack, ast);
            }
            else if (chr == ')')
            {
                while (op_stack && ((ast_t *)(op_stack->data))->op != PARENTHESIS)
                {
                    l_stack_push(&ret, l_stack_pop(&op_stack));
                }
                if (!op_stack)
                {
                    goto fail;
                }
                free(l_stack_pop(&op_stack));
            }
            else
            {
                goto fail;
            }
            break;
        }
    }
    if (val != -1)
    {
        ast_t *restrict ast = malloc(sizeof(ast_t));
        *ast = ast_from_val(val);
        l_stack_push(&ret, ast);
        val = -1;
    }
    while (op_stack)
    {
        l_stack_push(&ret, l_stack_pop(&op_stack));
        if (((ast_t *)(ret->data))->op == PARENTHESIS)
        {
            goto fail;
        }
    }
    l_stack_reverse(&ret);
    return ret;
fail:
    l_stack_free(op_stack, &free);
    l_stack_free(ret, &free);
    return NULL;
}

bool evaluate_postfix(intmax_t *restrict const out, l_stack_t const *restrict postfix)
{
    bool ret = true;
    l_stack_t *vals = NULL;
    for (l_stack_t const *cur = postfix; cur; cur = cur->prev)
    {
        ast_t *restrict ast = cur->data;
        intmax_t *restrict val;
        switch (ast->tag)
        {
        case VALUE:
            val = malloc(sizeof(intmax_t));
            *val = ast->val;
            l_stack_push(&vals, val);
            break;
        case OPERATOR:
            if (!vals || !vals->prev)
            {
                goto fail;
            }
            val = l_stack_pop(&vals);
            intmax_t right = *val;
            free(val);
            val = l_stack_pop(&vals);
            intmax_t left = *val;
            free(val);
            op_function *func = op_functions[ast->op];
            if (!func)
            {
                goto fail;
            }
            val = malloc(sizeof(intmax_t));
            *val = (*func)(left, right);
            l_stack_push(&vals, val);
            break;
        default:
            goto fail;
        }
    }
    if (!vals || vals->prev)
    {
        goto fail;
    }
    *out = *(intmax_t *)vals->data;
cleanup:
    l_stack_free(vals, &free);
    return ret;
fail:
    ret = false;
    goto cleanup;
}

int main(void)
{
    int ret = 0;
    printf("%s", msg_input);
    str_t *restrict input = read_line(stdin);
    l_stack_t *restrict postfix = parse_to_postfix(input);
    intmax_t calculated;
    printf("%s", msg_output);
    if (postfix && evaluate_postfix(&calculated, postfix))
    {
        printf("%" PRIdMAX, calculated);
    }
    else
    {
        printf("%s", error_msg);
    }
    l_stack_free(postfix, &free);
    str_free(input);
    return ret;
}
