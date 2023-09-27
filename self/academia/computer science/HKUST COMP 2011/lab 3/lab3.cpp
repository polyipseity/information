#include <iostream>
#include <fstream>
using namespace std;

const int NUM_LETTERS = 26;      // number of letters in the alphabet
const int NUM_DIGRAPHS = 676;    // number of all possible digraphs
const int MAX_PATH_LENGTH = 100; // maximum length of a file path

void number_to_diagraph(int num, char &c1, char &c2)
{

    // Convert a number to a diagraph
    // You **DO NOT** need to use this function in your implementation

    c1 = num / NUM_LETTERS + 'A';
    c2 = num % NUM_LETTERS + 'A';
}

void numbers_to_text(int num1, int num2, char &c1, char &c2, char &c3, char &c4)
{

    // Convert two numbers to a 4-letter text
    // You **DO NOT** need to use this function in your implementation

    number_to_diagraph(num1, c1, c2);
    number_to_diagraph(num2, c3, c4);
}

int digraph_to_number(char c1, char c2)
{

    // TODO: implement this function
    // Convert (c1, c2) to a number based on digraph coding
    // Return the converted number
    return 26 * (c1 - 'A') + (c2 - 'A');
    // End of TODO
}

int encrypt_digraph_to_number(char c1, char c2, int key)
{

    // TODO: implement this function
    // Encrypt the digraph (c1, c2) into a number using the key based on Caesar cipher
    // Return the encrypted number
    return digraph_to_number(c1, c2) + key;
    // End of TODO
}

void encrypt_text_to_numbers(char c1, char c2, char c3, char c4, int key, int &num1, int &num2)
{

    // TODO: implement this function
    // Call encrypt_digraph_to_number() to encrypt the 4-letter text using the key
    // Update the encrypted numbers (num1, num2)
    num1 = encrypt_digraph_to_number(c1, c2, key);
    num2 = encrypt_digraph_to_number(c3, c4, key);
    // End of TODO
}

int decrypt_digraph_to_number(char c1, char c2, int key)
{

    // TODO: implement this function
    // Decrypt the digraph (c1, c2) into a number using the key based on Caesar cipher
    // Return the decrypted number

    // End of TODO
}

void decrypt_text_to_numbers(char c1, char c2, char c3, char c4, int key, int &num1, int &num2)
{

    // TODO: implement this function
    // Call decrypt_digraph_to_number() to decrypt the 4-letter text using the key
    // Update the decrypted numbers (num1, num2)

    // End of TODO
}

int main()
{

    cout << "Welcome to Lab3: Encryption & Decryption!" << endl;

    // Read the input file path
    char file_path[MAX_PATH_LENGTH];
    cout << "Enter the input file name: ";
    cin >> file_path;
    ifstream fin(file_path);

    // Check if the file can be opened
    if (!fin)
    {
        cout << "Error: Can not open " << file_path << endl;
        return -1;
    }

    int option, key;
    char c1, c2, c3, c4;

    // TODO: fill this part
    // Read the option, the 4-letter text and the key from fin
    // Close the file after reading

    // End of TODO

    // Perform encryption or decryption
    if (option == 1)
    { // Encryption
        int num1, num2;
        char e1, e2, e3, e4;

        encrypt_text_to_numbers(c1, c2, c3, c4, key, num1, num2);
        numbers_to_text(num1, num2, e1, e2, e3, e4);

        cout << "The encrypted numbers are: " << num1 << " and " << num2 << endl;
        cout << "The encrypted text is: " << e1 << e2 << e3 << e4 << endl;
    }
    else if (option == 2)
    { // Decryption
        int num1, num2;
        char d1, d2, d3, d4;

        decrypt_text_to_numbers(c1, c2, c3, c4, key, num1, num2);
        numbers_to_text(num1, num2, d1, d2, d3, d4);

        cout << "The decrypted numbers are: " << num1 << " and " << num2 << endl;
        cout << "The decrypted text is: " << d1 << d2 << d3 << d4 << endl;
    }
    else
    {
        // You should not reach here
        cout << "Error: Invalid option " << option << endl;
        return -1;
    }

    return 0;
}