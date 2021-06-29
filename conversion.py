# imports
import json

# files
words = open("all_words.txt", "r")
database = open("database.json", "w")

# parameters
lines = words.readlines()
max_length = 0
min_length = 1e10

# first iteration
for line in lines:
    word = line.strip().strip("\n")
    length = len(word)

    if length > max_length:
        max_length = length

    if length < min_length:
        min_length = length

# database
database_dict = dict()
for length in range(min_length, max_length + 1):
    database_dict[length] = []

# second iteration
for line in lines:
    word = line.strip().strip("\n")
    length = len(word)

    database_dict[length].append(word)

# save
json.dump(database_dict, database, indent = 4)
