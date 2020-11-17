def only_nums(list):
    return [num for num in list if type(num) == int]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temps = [10, 11, 12, 14, 15]
    filtered = [temp for temp in temps if temp > 10]
    nums = only_nums([12, '1234', 40, 'ssdfsd'])
    ifelsed = [n if n > 0 else 9999 for n in [1, 2, 3, 45, 0]]
    print(filtered)
    print(nums)
    print(ifelsed)
