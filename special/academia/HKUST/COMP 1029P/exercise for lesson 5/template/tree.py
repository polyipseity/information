import turtle

# Super fast!
turtle.speed(0)

# Turn left for 90 degrees
# Complete this

def tree(trunkLength, currentDepth, maximumDepth):
    """ Draw a tree with turtle graphics recursively. """

    # Draw a trunk
    # Complete this

    if currentDepth < maximumDepth:
        # Turn left for 'angle' degrees
        # Complete this

        # Recursively draw a smaller tree
        # Complete this

        # Turn right for 2 * 'angle' degrees
        # Complete this

        # Recursively draw another smaller tree
        # Complete this

        # Turn left for 'angle' degrees, so that the
        # turtle faces its original starting direction
        # Complete this

    # Return to the original starting position
    # Complete this

# Run the tree function
# You can change the parameters to test it out
tree(100, 0, 5)
