# Madlib is a fill in the blank game where the user is prompted to fill in the blanks with their own words.
# CODE


noun=input("Enter a noun: ")
adjective=input("Enter an adjective: ")
adjective2=input("Enter another adjective: ")
noun2=input("Enter another noun: ")
verb=input("Enter a verb: ")

sentence = f"Every person has their own {noun},some people are {adjective} and some people are {adjective2}.\
    Its a {noun2} world out there and we all have to {verb} it."

print(sentence)