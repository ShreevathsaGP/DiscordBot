# imports
import json

# files
database = open("database.json", "r")
database_dict = json.load(database)

# char dict
sample_dict = dict()
for ascii_digit in range(97, 123):
    sample_dict[chr(ascii_digit)] = 0

# count chars
def count(string):
    return_dict = sample_dict.copy()
    for char in string:
        return_dict[char] += 1

    return return_dict

# compare counts
def same_count(one, two):
    for ascii_digit in range(97, 123):
        if one[chr(ascii_digit)] != two[chr(ascii_digit)]:
            # print(one[chr(ascii_digit)], two[chr(ascii_digit)])
            return False

    return True

# solve scramble
def solve_scramble(scramble):
    scramble = scramble.strip()
    scramble_count = count(scramble)
    length = str(len(scramble))

    solutions = []
    
    for word in database_dict[length]:
        word_count = count(word)

        if same_count(scramble_count, word_count):
            solutions.append(word)

    return solutions
