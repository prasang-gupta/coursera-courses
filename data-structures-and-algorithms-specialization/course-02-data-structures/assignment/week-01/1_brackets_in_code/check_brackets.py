# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) > 0:
                if are_matching(opening_brackets_stack[-1].char, next):
                    opening_brackets_stack.pop()
                else:
                    return i + 1
            else:
                return i + 1
    if len(opening_brackets_stack) == 0:
        return 0
    return opening_brackets_stack[-1].position + 1


def main():
    text = input()
    # text = "[]"
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
