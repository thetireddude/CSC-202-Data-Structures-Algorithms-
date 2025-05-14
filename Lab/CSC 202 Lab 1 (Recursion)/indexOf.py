def indexOf(text, substring, index = 0):

    if text[index: index + len(substring)] == substring:
        return index
    if len(text) < len(substring):
        return -1

    return indexOf(text, substring, index + 1)



print(indexOf("Mississippi", "sip"))

# for languages that dont allow us to pass in a default value for a parameter like we did for index (eg - java)
# use a helper function
# main function calls the helper function
# the recursive call happens inside of the helper function