// Please don't include any extra libraries in your homework. We already included all necessary libraries in the skeleton code.
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

char const error_msg_decimal[] = "Error! That set of number is not a decimal number.\n";
char const error_msg_trinary[] = "Error! That set of number is not a trinary number.\n";
char const error_msg_duodecimal[] = "Error! That set of number is not a duodecimal number.\n";
char const error_msg_unsupported_system[] = "Error! The number system is not supported.\n";
char const msg_prompt_number[] = "Please enter a set of number:\n";
char const msg_prompt_current_number_system[] = "Please enter the current number system:\n";
char const msg_prompt_number_system_to_convert[] = "Please enter the number system you want the set of number be converted to:\n";
char const msg_output[] = "Output=";
int_fast8_t const digits_c2i[] = {
    ['0'] = 0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    ['a'] = 10,
    11,
    ['A'] = 10,
    11,
};
char const digits_i2c[] = "0123456789AB";

int main()
{
    char const *const error_msgs_system[] = {
        [3] = error_msg_trinary,
        [10] = error_msg_decimal,
        [12] = error_msg_duodecimal,
    };
    char input[42];
    printf("%s", msg_prompt_number);
    scanf("%s", &input);

    /**
     * @brief
     * Get user input for number to be convert
     */

    // TODO:
    signed char base;
    printf("%s", msg_prompt_current_number_system);
    scanf("%hhd", &base);
    if (base != 3 && base != 10 && base != 12)
    {
        printf("%s", error_msg_unsupported_system);
        return 0;
    }
    uint_fast64_t val = 0;
    for (int ii = 0; input[ii] != '\0'; ++ii)
    {
        int_fast8_t digit = input[ii] < sizeof digits_c2i / sizeof(int_fast8_t) ? digits_c2i[input[ii]] : 0;
        if (digit >= base || digit == 0 && input[ii] != '0')
        {
            printf("%s", error_msgs_system[base]);
            return 0;
        }
        val *= base;
        val += digit;
    }

    /**
     * @brief
     * Get user input for current number system
     */

    // TODO:
    signed char new_base;
    printf("%s", msg_prompt_number_system_to_convert);
    scanf("%hhd", &new_base);
    if (new_base != 3 && new_base != 10 && new_base != 12)
    {
        printf("%s", error_msg_unsupported_system);
        return 0;
    }

    /**
     * @brief
     * Get user input for the number system for conversion.
     * Print converted number in format of "Output=12", e.g Output=ABCDEF
     * No space should be inserted in the asnwer "Output=XXX".
     * In case of wrong number system for conversion, please use the above error msgs.
     */

    // TODO:
    printf("%s", msg_output);
    if (val == 0)
    {
        printf("0\n");
        return 0;
    }
    char output[sizeof input / sizeof(char) - 1];
    int_fast8_t len = 0;
    while (val != 0)
    {
        ++len;
        output[sizeof output / sizeof(char) - len] = digits_i2c[val % new_base];
        val = val / new_base;
    }
    printf("%.*s\n", len, &output[sizeof output / sizeof(char) - len]);

    return 0;
}
// C programmers never die. They are just cast into void.
