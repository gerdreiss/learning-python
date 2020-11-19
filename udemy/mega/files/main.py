import os
import sys


# Press the green button in the gutter to run the script.
def read_file_if_exists(path):
    print("=" * 50)
    print("read_file_if_exists:")
    if os.path.exists(path):
        with open(path) as f:
            print(f.read())
    else:
        print("File does not exist.")


def read_fruits():
    global f, content
    print("=" * 50)
    with open("data/fruits.txt") as f:
        content = f.read()
    print(content)
    print(len([letter for letter in content if letter == 'a']))


def write_veggies():
    global f
    print("=" * 50)
    with open("data/veggies.txt", "a+") as f:
        f.write("cucumber\n")
        f.write("eggplant\n")
        f.write("garlic\n")
        f.seek(0)
        print(f.read())


def duplicate_veggies():
    global f, content
    print("=" * 50)
    with open("data/fruits.txt", "a+") as f:
        f.seek(0)
        content = f.read()
        print(content)
        f.write(content)
        f.write(content)


if __name__ == '__main__':
    # f = open("fruits.txt")
    # content = f.read()
    # f.close()

    # read_fruits()
    # write_veggies()
    # duplicate_veggies()

    read_file_if_exists("data/fruits.txt")
