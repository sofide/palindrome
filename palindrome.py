import sys

sys.setrecursionlimit(10**5)

FILEPATH_TEMPLATE = "inputs/PALIN{}.IN"

FILES = [
    FILEPATH_TEMPLATE.format(n)
    for n in range(1, 11)
]

insertions_cache = {}


def insertions_to_palindrome(text: str) -> int:
    """
    Return the minimum quantity of insertions needed to convert the given text in a
    palindrome.
    """
    if text in insertions_cache:
        return insertions_cache[text]

    first_index = 0  # index of the first character
    last_index = len(text) - 1  # index of the las character

    # check if the extremes are equal to reduce the problem in a smaller slice of text
    while text[first_index] == text[last_index]:
        if first_index >= last_index:
            # if all the extrems are equal, no insertions are needed: the text already
            # is a palindrome
            insertions_cache[text] = 0
            return 0
        first_index += 1
        last_index -= 1

    # here first_index and last_index are the first non-equal extremes

    # calc the remaining insertions needed if we insert a character equal to
    # text[last_index] at the left of first_index
    insertions_if_insert_left = insertions_to_palindrome(text[first_index:last_index])

    # calc the remaining insertions needed if we insert a character equal to
    # text[first_index] at the right of last_index
    insertions_if_insert_right = insertions_to_palindrome(
        text[first_index + 1:last_index + 1]
    )

    # select the path with the minimum quantity of insertions required and add the
    # current insertion
    insertions = min(insertions_if_insert_left, insertions_if_insert_right) + 1
    insertions_cache[text] = insertions
    return insertions


def solve_excercice(filepath):
    print("-"*50)
    print(f"solving {filepath}")
    with open(filepath) as file:
        text = file.readlines()
        size, text = text
        print(f"the size of the file is {size}")
        text = text.strip()
    result = insertions_to_palindrome(text)
    print(f"result = {result}")
    print("-"*50)


if __name__ == "__main__":
    print("- Insert a number from 1 to 10 process a specific excercise.")
    print(
        "- Insert any other text to calculate how many insertions are needed to " \
        "convert it in a palindrome."
    )
    print("- Or press enter to run all the excercices")

    user_input = input()

    if user_input == "":
        for  filepath in FILES:
            solve_excercice(filepath)

    else:
        try:
            solve_excercice(FILEPATH_TEMPLATE.format(user_input))

        except FileNotFoundError:
            print(f"calculating insertions to make a palindrome from '{user_input}'")
            print(insertions_to_palindrome(user_input))
