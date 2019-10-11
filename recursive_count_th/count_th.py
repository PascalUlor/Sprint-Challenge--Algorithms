'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    if word == "":
        return 0

    if word[:2] == 'th':
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])
    # pass


print(count_th('thousandth'))

"""
1. Create a list from the word input
2. slice out the first two letters
"""