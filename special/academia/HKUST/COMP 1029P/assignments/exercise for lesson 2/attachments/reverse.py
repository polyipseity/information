def reverse(word):
    """ Reverses the order of an input word and return the
    result """

    result = ""
    for letter in word:
        result = letter + result
    return result
