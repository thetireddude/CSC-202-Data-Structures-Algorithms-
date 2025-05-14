from stack_linked_list import StackLinkedList


def string_checker(input_string):

    stack = StackLinkedList(100)

    symbols_of_interest = {
        "}":"{", ")":"(", "]":"[" }

    for char in input_string:
        if char in symbols_of_interest.values():
            stack.push(char)
        elif char in symbols_of_interest:
            if not stack.is_empty():
                if symbols_of_interest[char] == stack.peek():
                    stack.pop()
                else:
                    return False
            else:
                return False

    if stack.is_empty():
        return True
    else:
        return False





