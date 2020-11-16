# coding=utf-8
# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    if phrase.startswith(("how", "what", "where", "why")):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sentences = []
    while True:
        user_input = input("Say something: ")
        if user_input == "\\end":
            break
        else:
            sentences.append(sentence_maker(user_input))
    print(" ".join(sentences))
