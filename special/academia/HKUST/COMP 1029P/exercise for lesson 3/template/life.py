import time # Required for time.sleep

# You implemented this neighbors() function previously in
# Review Questions 3.1
def neighbors(currentGen, row, column):
    """ This function takes a 2D array and the row number and
    the column number of the target cell and returns the
    number of neighbor cells that are 1. """

    count = 0

    # Handle boundary case for the row number
    if row - 1 < 0:
        minRow = 0
    else:
        minRow = row - 1

    # Handle boundary case for the column number
    if column - 1 < 0:
        minCol = 0
    else:
        minCol = column - 1

    # Use slicing to get the rows
    for rows in currentGen[minRow:row+2]:
        # Use slicing to get the cells
        for cell in rows[minCol:column+2]:
            # Increase count by 1 if the cell is 1
            # Complete this

    # Reduce count by 1 if the target cell is also 1
    # Complete this

    # Return the number of neighbors
    return count


# You implemented this nextgen() function previously in
# Review Questions 3.2
def nextgen(currentGen):
    """ This function takes a 2D array and returns the next
    generation according to the rules of Conway's Game of
    Life. This function uses neighbors() shown above. """

    # Initialize the output as an empty array
    output = []

    # Handle the input row by row
    for row in range(len(currentGen)):
        # Create a new row
        newRow = []

        # Handle the input row cell by cell
        for col in range(len(currentGen[row])):
            newRow.append(0) # Delete this line

            # Calculate the number of neighbors that are 1
            # Complete this

            # Check the status of the current cell, i.e. the
            # number of neighbors, and update the cell using
            # the rules of Conway's Game of Life

            # If the current cell is 0:
                # If there are exactly 3 neighbors:
                    # The current cell in the next generation
                    # has a 1
                # Else:
                    # The current cell in the next generation
                    # has a 0. Use newRow.append(0) to add a 0
                    # at the end of the list newRow

            # Else if the current cell is 1:
                # If there are 2 or 3 neighbors, the current
                # cell in the next generation has a 1, else it
                # has a 0.

        # Add the new row to the output array
        # Complete this

    # Return the 2D array representing the next generation
    return output


# This print_life() function is given to you and is already
# working. You should not change this function.
def print_life(currentGen):
    """ This function prints the input 2D array. Every cell
    that is 1 is printed as a '#' and every cell that is 0
    is printed as an empty space. """

    # Initialize the output as an empty string
    output = ""

    # Handle the input array row by row
    for row in currentGen:
        # Handle each row cell by cell
        for cell in row:
            # If the current cell is 0:
            if cell == 0:
                # Add a ' ' to the output string
                output = output + " "
            else:
                # Add a '#' to the output string
                output = output + "#"
        # When finished handling a row, add a '\n' (new line)
        # to the output string
        output = output + "\n"

    # Add an extra empty line at the very end of the output
    output = output + "\n"

    # Print the output
    print(output)


def life(currentGen, generation):
    """ This function implements Conway's Game of Life. """

    # First of all, clear the screen
    # Complete this

    # Print the message "Initial generation:"
    # Complete this

    # Print the initial generation of the 2D array
    # Complete this

    # Delay for 1 second (or 0.5 second)
    # Complete this

    # Put the input 2D array into the newGen variable
    # so that the for loop can iterate using newGen below
    newGen = currentGen

    # Generate and print the next generation for 'generation'
    # number of times, with a 1 second delay between each
    # generation.
    # Complete this with a for loop:
        # Inside this loop, you need to do these:
        # 1. Generate the next generation using the function
        # nextgen(). The 2D array of the next generation is
        # directly stored into 'newGen'.
        # Complete this

        # 2. Clear the screen
        # Complete this

        # 3. Print the message "Generation n:" where n is a
        # number.
        # Complete this

        # 4. Print the new generation
        # Complete this

        # 5. Delay for 1 second (or 0.5 second)
        # Complete this


# Here is a simple 2D array to test your work

start = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


# Here are some interesting 2D arrays with initial values

tumbler = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
# It's better if you use at least 30 for the number of
# generations

face = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
# It's better if you use at least 30 for the number of
# generations

glider_gun = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
# It's better if you use at least 50 for the number of
# generations
