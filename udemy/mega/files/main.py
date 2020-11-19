# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # f = open("fruits.txt")
    # content = f.read()
    # f.close()

    print("=" * 50)

    with open("data/fruits.txt") as f:
        content = f.read()

    print(content)
    print(len([letter for letter in content if letter == 'a']))

    print("=" * 50)

    with open("data/veggies.txt", "a+") as f:
        f.write("cucumber\n")
        f.write("eggplant\n")
        f.write("garlic\n")
        f.seek(0)
        print(f.read())

    print("=" * 50)

    with open("data/fruits.txt", "a+") as f:
        f.seek(0)
        content = f.read()
        print(content)
        f.write(content)
        f.write(content)
