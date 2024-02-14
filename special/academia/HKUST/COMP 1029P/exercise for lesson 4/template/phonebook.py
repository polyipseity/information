"""
In this exercise, three functions represent three database utilities:

    - db_create
    - db_add
    - db_query

The utilities are used in the main menu which is shown at the start.
"""

def db_create():
    """ Create a new database with some data """

    # Ask the user for the file name of the database
    # Modify this using input()
    filename = ""

    # Open the file for writing
    # Modify this using open()
    db = filename

    # Ask the user for the name of the new contact
    # Modify this using input()
    name = ""

    # Now we will use a while loop to repeatedly ask for new
    # contacts.

    # The while loop ends when the entered name is "done".
    while name != "done":
        # 1. Ask the user for the phone number
        # Modify this using input()
        number = ""

        # 2. Write the new contact to the database file
        # Complete this using db.write() for the name and number

        # 3. Ask the user for the name of the new contact
        # Modify this using input()
        name = "done"

    # Say "Done."
    print("Done.")
    print()

    # Close the database file
    # Complete this by closing the file db


# This function, db_add(), is already completed for you.
# This is given to you. You do not need to change it.
def db_add():
    """ Add new entries to an existing database """

    # Keep trying until we have a valid file name
    while True:
        try:
            # Ask the user for the file name of the database
            filename = input("Enter the filename of the database: ")

            # Try reading the file with the given name
            db = open(filename, "r")
        except IOError: # If the file does not exist
            print("There is no file by that name. Try again...")
        else: # No problem opening the file
            # Close it
            db.close()

            # Open the file again for appending new contact data
            db = open(filename, "a")

            # Exit the infinite while loop
            break

    # Ask the user for the name of the new contact
    name = input("Enter a name: ")

    # Data input ends when the entered name is "done".
    # Keep asking the user for contact data.
    while name != "done":
        # Ask the user for the phone number of the new contact
        number = input("Enter a phone number: ")

        # Write the new contact to the database file
        db.write(name + "\n")
        db.write(number + "\n")

        # Ask the user for the name of the new contact
        name = input("Enter a name: ")

    # Say "Done."
    print("Done.")
    print()

    # Close the database file
    db.close()


def db_query():
    """ Retrieve contact data from the database """

    # Keep trying until we successfully read
    # an existing database file
    while True:
        try:
            # Ask the user for the file name of the database
            # Modify this using input()
            filename = ""

            # Try reading the file with the given name
            # Modify this using open()
            db = filename
        except IOError: # If the file does not exist
            print("There is no file by that name. Try again...")
        else: # No problem opening the file
            # Read all the lines from the file
            # Modify this by reading the lines from the file db
            data = ["Name\n", "Number\n"]

            # Close the file
            # Complete this by closing the file db

            break

    # Create the phone book, an empty dictionary
    phonebook = {}

    # Remove all the '\n' from the data loaded from the file
    # Modify this for loop to "slice" off the last '\n'
    for i in range(len(data)):
        data[i] = data[0:]

    # Now we will use a for loop to go through all the lines
    # of the data loaded from the file (already done above),
    # two lines at once. The first line is the contact name
    # and the second line is the phone number.
    for i in range(0, len(data), 2):
        # Add new contact into the dictionary
        # Modify this using the data list
        phonebook["Name"] = "Number"

    # Ask the user for the name to be searched for
    # Modify this using input()
    name = ""

    # Now we will use a while loop to repeatedly ask for names
    # to be searched for.
    # The while loop ends when the entered name is "done".
    while name != "done":
        # 1. Check if the contact name can be found in
        #    the phone book
        #    1.1. If yes, then show the phone number
        #    1.2. If no, then show an error message

        # 2. Ask the user for the name to be searched for
        # Modify this using input()
        name = "done"

    # Say "Done."
    print("Done.")
    print()

# Show the main menu
choice = ""
while choice != "x":
    print("Welcome the phone book database system!")
    print()
    print("Please select from one of the following:")
    print()
    print("  c - Create a new phone book database")
    print("  a - Add a new entry to an existing phone book database")
    print("  q - Make queries from an existing phone book database")
    print()
    print("  x - Exit the system")
    print()

    choice = input("(c/a/q/x): ")

    if choice == "c":
        db_create()
    elif choice == "a":
        db_add()
    elif choice == "q":
        db_query()

print("Bye!")
