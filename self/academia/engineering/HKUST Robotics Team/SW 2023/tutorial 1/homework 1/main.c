#include <math.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include "ast.h"
#include "l_stack.h"
#include "str.h"

char const *const msg_input = "Please input a math equation:\n";
char const *const msg_output = "Output:\n";
char const *const error_msg = "ERROR! The string input is not supported!!\n";

str_t *read_line(FILE *stream)
{
    str_t *ret = str_malloc(0);
    for (char cc = getc(stream); cc != EOF && cc != '\n'; cc = getc(stream))
    {
        size_t idx = ret->len;
        str_realloc(&ret, idx + 1);
        ret->data[idx] = cc;
    }
    return ret;
}

l_stack_t *parse_to_postfix(str_t const *input)
{
    l_stack_t *ret = NULL, *op_stack = NULL;
    ast_t *ast;
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
                ast = malloc(sizeof(ast_t));
                *ast = ast_from_val(val);
                l_stack_push(&ret, ast);
                val = -1;
            }
            switch (chr)
            {
            case '+':
            case '-':
            case '*':
            case '/':
            case '^':
            case '(':
                op_t op = op_from_char(chr);
                if (op != PARENTHESIS)
                {
                    while (op_stack && priorities[((ast_t *)(op_stack->data))->op] >= priorities[op])
                    {
                        l_stack_push(&ret, l_stack_pop(&op_stack));
                    }
                }
                ast = malloc(sizeof(ast_t));
                *ast = ast_from_op(op);
                l_stack_push(&op_stack, ast);
                break;
            case ')':
                while (op_stack && ((ast_t *)(op_stack->data))->op != PARENTHESIS)
                {
                    l_stack_push(&ret, l_stack_pop(&op_stack));
                }
                if (!op_stack)
                {
                    goto fail;
                }
                free(l_stack_pop(&op_stack));
                break;
            default:
                goto fail;
            }
        }
    }
    if (val != -1)
    {
        ast = malloc(sizeof(ast_t));
        *ast = ast_from_val(val);
        l_stack_push(&ret, ast);
        val = -1;
    }
    while (op_stack)
    {
        l_stack_push(&ret, l_stack_pop(&op_stack));
        if (ast->op == PARENTHESIS)
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

bool evaluate_postfix(double *const out, l_stack_t const *postfix)
{
    bool ret = true;
    l_stack_t *vals = NULL;
    for (l_stack_t const *cur = postfix; cur; cur = cur->prev)
    {
        ast_t *ast = cur->data;
        double *val;
        switch (ast->tag)
        {
        case VALUE:
            val = malloc(sizeof(double));
            *val = (double)ast->val;
            l_stack_push(&vals, val);
            break;
        case OPERATOR:
            if (!vals || !vals->prev)
            {
                goto fail;
            }
            double *right_p = l_stack_pop(&vals), *left_p = l_stack_pop(&vals);
            double right = *right_p, left = *left_p;
            free(left_p);
            free(right_p);
            val = malloc(sizeof(double));
            switch (ast->op)
            {
            case PLUS:
                *val = left + right;
                break;
            case MINUS:
                *val = left - right;
                break;
            case MULTIPLY:
                *val = left * right;
                break;
            case DIVIDE:
                *val = left / right;
                break;
            case POWER:
                *val = pow(left, right);
                break;
            default:
                free(val);
                goto fail;
            }
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
    *out = *(double *)vals->data;
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
    printf_s("%s", msg_input);
    str_t *input = read_line(stdin);
    l_stack_t *postfix = parse_to_postfix(input);
    double calculated;
    if (!postfix || !evaluate_postfix(&calculated, postfix))
    {
        goto fail;
    }

    printf_s("%s", msg_output);
    printf_s("%g", calculated);
cleanup:
    l_stack_free(postfix, &free);
    str_free(input);
    return ret;
fail:
    printf_s("%s", error_msg);
    ret = 1;
    goto cleanup;
}
