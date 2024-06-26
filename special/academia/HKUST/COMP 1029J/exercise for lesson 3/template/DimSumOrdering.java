import java.util.Scanner;

/**
 * This class creates 4 DimSum dishes, provides an interface for users
 * to order, and print out the order summary after the ordering
 *
 * The four dim sum dishes are:
 *   Barbecued Pork Bun
 *   Shrimp Dumpling
 *   Siu Mai
 *   Spring Roll
 */
public class DimSumOrdering
{
    // This stores the dim sum dishes in the system
    DimSum[] dishes;

    // The constructor of DimSumOrdering
    public DimSumOrdering()
    {
        //
        // Task 2 - Initialize the dim sum dishes in the system
        //
    }

    // Start the ordering system
    public void start() {
        // Prepare a scanner for reading the input
        Scanner scanner = new Scanner(System.in);

        int i;
        String choice;
        do {
            // Print the menu
            System.out.println("Welcome to the G/F restaurant!");
            System.out.println("Please order your dim sum dishes:");
            System.out.println();

            //
            // Task 2 - Print the choices using a loop
            //

            System.out.println("5) Bill and payment");
            System.out.println();
            System.out.print("Please enter 1, 2, 3, 4 or 5: ");

            // Read the input
            choice = scanner.next();

            //
            // Task 2 - Based on the choice add the order
            //

            System.out.println();
        } while (!choice.equals("5"));

        // Show the bill
        showBill();
    }

    // Show the order
    public void showBill() {
        System.out.println("Qty\tAmt\tDish");
        System.out.println("----------------------------------");

        //
        // Task 3 - Print the bill summary
        //

        System.out.println("----------------------------------");

        //
        // Task 3 - Calculate and print the total amount
        //
    }

    // The main method to start the program
    public static void main(String[] args) {
        DimSumOrdering ordering = new DimSumOrdering();
        ordering.start();
    }

}
