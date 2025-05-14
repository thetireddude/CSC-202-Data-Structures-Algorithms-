def indexOf(text, substring):

    if text[: len(substring)] == substring:
        return 0

    return helper(text, substring, 0)


def helper(text, substring, index):

    if len(text[index : ]) < len(substring):
        return -1

    if text[index : index + len(substring)] == substring:
        return index

    return helper(text, substring, index + 1)

print(indexOf("worldellohaha", "hello"))