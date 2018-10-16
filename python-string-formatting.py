def print_formatted(number):
    # your code goes here

    # Calculating length of binary representation of number
    i = 1
    while (number >= 2 ** i):
        i += 1

    for j in range(1, number + 1):
        print("{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}".format(j, i))