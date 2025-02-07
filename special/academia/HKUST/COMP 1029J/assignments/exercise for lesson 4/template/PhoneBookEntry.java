/**
 * This class handles one entry of the phone book.
 */

public class PhoneBookEntry
{
    // Store the name of the entry
    String name;

    // Store the number of the entry
    String number;

    // A constructor using the line as input
    public PhoneBookEntry(String line) {
        // Split the line into two parts
        String[] parts = line.split(":");

        // Store the name and number
        name = parts[0];
        number = parts[1];
    }

    // A constructor using the name and number as input
    public PhoneBookEntry(String newname, String newnumber) {
        name = newname;
        number = newnumber;
    }

    // Return the name of the entry
    public String getName() {
        return name;
    }

    // Return the number of the entry
    public String getNumber() {
        return number;
    }

    // Change the entry to a data line
    public String toLine() {
        return name + ":" + number;
    }

    // Print the entry to the screen
    public void print() {
        // Print a padded name
        System.out.print(name);
        int i;
        for (i = name.length(); i < 10; i++) {
            System.out.print(" ");
        }

        // Print the number
        System.out.print(number);
    }
}
