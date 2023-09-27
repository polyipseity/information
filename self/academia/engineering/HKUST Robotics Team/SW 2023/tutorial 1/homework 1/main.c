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

void read_line(str_t **ret, FILE *stream)
{
    for (char cc = getc(stream); cc != EOF && cc != '\n'; cc = getc(stream))
    {
        size_t idx = (*ret)->len;
        *ret = str_realloc(*ret, idx + 1);
        (*ret)->data[idx] = cc;
    }
}

l_stack_t *parse(str_t *input)
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
                ret = l_stack_push(ret, ast);
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
                        op_stack = l_stack_pop(op_stack, &ast);
                        ret = l_stack_push(ret, ast);
                    }
                }
                ast = malloc(sizeof(ast_t));
                *ast = ast_from_op(op);
                op_stack = l_stack_push(op_stack, ast);
                break;
            case ')':
                while (op_stack && ((ast_t *)(op_stack->data))->op != PARENTHESIS)
                {
                    op_stack = l_stack_pop(op_stack, &ast);
                    ret = l_stack_push(ret, ast);
                }
                if (!op_stack)
                {
                    goto fail;
                }
                op_stack = l_stack_pop(op_stack, &ast);
                free(ast);
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
        ret = l_stack_push(ret, ast);
        val = -1;
    }
    while (op_stack)
    {
        op_stack = l_stack_pop(op_stack, &ast);
        ret = l_stack_push(ret, ast);
        if (ast->op == PARENTHESIS)
        {
            goto fail;
        }
    }
    return ret;
fail:
    l_stack_free(op_stack, &free);
    l_stack_free(ret, &free);
    return NULL;
}

int main(void)
{
    printf_s("%s", msg_input);
    str_t *input = str_malloc(0);
    read_line(&input, stdin);
    l_stack_t *asts = parse(input), *vals = NULL;
    if (!asts)
    {
        goto fail;
    }
    asts = l_stack_reverse(asts);

    while (asts)
    {
        ast_t *ast;
        asts = l_stack_pop(asts, &ast);
        double *val;
        switch (ast->tag)
        {
        case VALUE:
            val = malloc(sizeof(double));
            *val = (double)ast->val;
            vals = l_stack_push(vals, val);
            break;
        case OPERATOR:
            if (!vals || !vals->prev)
            {
                free(ast);
                goto fail;
            }
            double *right_p, *left_p;
            vals = l_stack_pop(vals, &right_p);
            vals = l_stack_pop(vals, &left_p);
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
                free(ast);
                goto fail;
            }
            vals = l_stack_push(vals, val);
            break;
        default:
            free(ast);
            goto fail;
        }
        free(ast);
    }
    if (!vals || vals->prev)
    {
        goto fail;
    }
    printf_s("%s", msg_output);
    printf_s("%g", *(double *)vals->data);
cleanup:
    l_stack_free(vals, &free);
    l_stack_free(asts, &free);
    str_free(input);
    return 0;
fail:
    printf_s("%s", error_msg);
    goto cleanup;
}
