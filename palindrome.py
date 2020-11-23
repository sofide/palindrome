FILEPATH_TEMPLATE = "inputs/PALIN{}.IN"

FILES = [
    FILEPATH_TEMPLATE.format(n)
    for n in range(1, 11)
]

calc_cache = {}


def insertions_to_make_palindrome(text):
    first_char = text[0]
    last_char = text[-1]

    if len(text) <= 2:
        if first_char == last_char:
            return 0
        return 1

    if text in calc_cache:
        return calc_cache[text]

    if first_char == last_char:
        insertions = insertions_to_make_palindrome(text[1:-1])
        calc_cache[text] = insertions
        return insertions

    insertions_if_insert_left = insertions_to_make_palindrome(text[:-1])
    insertions_if_insert_right = insertions_to_make_palindrome(text[1:])

    insertions = min(insertions_if_insert_left, insertions_if_insert_right) + 1
    calc_cache[text] = insertions
    return insertions


def solve_excercice(filepath):
    print(f"solving {filepath}")
    with open(filepath) as file:
        text = file.readlines()
        size, text = text
        print(f"the size of the file is {size}")
        text = text.strip()
    result = insertions_to_make_palindrome(text)
    print(f"result = {result}")


if __name__ == "__main__":
    print("Put a number from 1 to 10 process a specific excercise")
    print("Insert any other text to calculate how many insertions are needed to make it a palindrome")
    print("Or press enter to run all the excercices")

    user_input = input()

    if user_input == "":
        for  filepath in FILES:
            solve_excercice(filepath)

    else:
        try:
            solve_excercice(FILEPATH_TEMPLATE.format(user_input))

        except FileNotFoundError:
            print(f"calculating insertions to make a palindrome from '{user_input}'")
            print(insertions_to_make_palindrome(user_input))
