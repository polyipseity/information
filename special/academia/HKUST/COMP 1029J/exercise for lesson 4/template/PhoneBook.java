/**
 * This class is the main class of the phone book program.
 */
import java.util.Scanner;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.nio.file.StandardOpenOption;
import java.nio.charset.Charset;
import java.io.BufferedReader;
import java.io.BufferedWriter;

public class PhoneBook
{
    // Prepare a scanner for reading inputs
    Scanner scanner = new Scanner(System.in);

    // Show the main menu of the program
    public void mainmenu()
    {
        System.out.println("Welcome to the phone book program.");
        System.out.println();

        String choice;
        do {
            // Print the main menu
            System.out.println("Please choose one of the following:");
            System.out.println();

            System.out.println("1) Add New Phone Number");
            System.out.println("2) List Phone Numbers");
            System.out.println("3) Find Phone Number by Name");
            System.out.println("4) Delete Phone Number by Name");
            System.out.println("5) Quit");
            System.out.println();

            System.out.print("Please enter 1, 2, 3, 4 or 5: ");

            // Get the selection from the user
            choice = scanner.next();

            // Based on the selection run the appropriate method
            switch (choice) {
                case "1":
                    addNumber();
                    break;
                case "2":
                    listNumbers();
                    break;
                case "3":
                    findNumberByName();
                    break;
                case "4":
                    deleteNumberByName();
                    break;
            }

            System.out.println();
        } while (!choice.equals("5"));

        System.out.println("Bye!");
    }

    // Check whether the name exists in the current phone book
    public boolean exists(String name) {
        //
        // Task 1 - Checking for duplicated new entry
        //
        
        // Get the path of the text file
       
        // Use a BufferedReader to read the data one by one
        
        // For each data line create a PhoneBookEntry

        // If the name in the PhoneBookEntry is equal to the input name
        // return true
        
        
        // Return false if nothing matches the input name
        return false;
    }

    // Add a new entry to the phone book
    public void addNumber() {
        // Get the name
        System.out.print("Please enter the name: ");
        String name = scanner.next();

        // Get the number
        System.out.print("Please enter the number: ");
        String number = scanner.next();

        // Check whether the name already exists, if so,
        // print a message and exit the method
        if (exists(name)) {
            System.out.println("Phone number entry already exists!");
            return;
        }

        // Get the path of the text file
        Path path = Paths.get("phonebook.txt");
        
        try {
            // Get a BufferedWriter from the file
            BufferedWriter writer =
                Files.newBufferedWriter(path, Charset.defaultCharset(),
                                        StandardOpenOption.APPEND);

            // Create a new phone book entry from the data
            PhoneBookEntry entry = new PhoneBookEntry(name, number);

            // Add a new phone number in a line
            writer.write(entry.toLine());
            writer.newLine();

            // Close the writer
            writer.close();
        }
        catch (Exception e) {
            System.out.println("I have some problems writing the file!");
        }
    }

    // List the current entries in the phone book
    public void listNumbers() {
        // Get the path of the text file
        Path path = Paths.get("phonebook.txt");
        
        try {
            // Get a BufferedReader from the file
            BufferedReader reader =
                Files.newBufferedReader(path, Charset.defaultCharset());

            // Read the content line-by-line and print it out
            String line;
            while ((line = reader.readLine()) != null) {
                // Create a new phone book entry from the data line
                PhoneBookEntry entry = new PhoneBookEntry(line);

                // Print the phone book entry
                entry.print();
                System.out.println();
            }
        }
        catch (Exception e) {
            System.out.println("I have some problems reading the file!");
        }
    }

    // Find an entry in the phone book by name
    public void findNumberByName() {
        // Get the name
        System.out.print("Please enter the name: ");
        String name = scanner.next();

        //
        // Task 2 - Finding and printing an entry by name
        //
        
        // Get the path of the text file
       
        // Use a BufferedReader to read the data one by one
        
        // For each data line create a PhoneBookEntry

        // If the name in the PhoneBookEntry is equal to the input name
        // print the PhoneBookEntry appropriately and exit the method
        
        // Print a message if the name cannot be found
        

    }

    // Delete an entry in the phone book by name
    public void deleteNumberByName() {
        // Get the name
        System.out.print("Please enter the name: ");
        String name = scanner.next();

        // Prepare an array to store the phone number entries
        PhoneBookEntry[] entries = new PhoneBookEntry[100];

        // Store the number of entries in the phone book
        int numOfEntries = 0;

        //
        // Task 3 - Deleting a phone book entry by name
        //
        
        // Get the path of the text file
       
        // Use a BufferedReader to read the data one by one
        
        // For each data line create a PhoneBookEntry

        // If the name in the PhoneBookEntry is NOT equal to the input name
        // add the entry to the entries array
        
        // Use a BufferedWriter to write the stored data from the array into
        // the text file one by one

        // Close the BufferedWriter


    }

    // The main method to start the phone book program
    public static void main(String[] args)
    {
        // Start the phone book program
        PhoneBook phonebook = new PhoneBook();
        phonebook.mainmenu();
    }
}
