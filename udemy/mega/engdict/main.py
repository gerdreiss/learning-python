import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def select_one(matches):
    for i, match in enumerate(matches):
        print(" %s - %s" % (i, match))

    len_matches = len(matches)
    print(" %s - None of the above" % len_matches)

    answer = input("Please select between 0 and %s " % len_matches).strip()

    if not answer.isdigit():
        print("Invalid input. Please, try again")
        return select_one(matches)

    index = int(answer)
    if index > len_matches:
        print("Invalid input. Please, try again")
        return select_one(matches)

    if index == len_matches:
        return "The word does not exist."

    return translate(matches[index])


def translate(w):
    if w in data:
        return data[w]

    if w.lower() in data:
        return data[w.lower()]

    if w.title() in data:
        return data[w.title()]

    if w.upper() in data:
        return data[w.upper()]

    matches = get_close_matches(word=w, possibilities=data.keys(), n=4, cutoff=0.75)

    if len(matches) == 0:
        return "The word does not exist."

    print("Did you mean one of the following instead?")
    return select_one(matches)


word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
