def swap_case(s):
    swapped_list = []
    for i in s:
        # print(i)
        if i.isupper():
            swapped_list.append(i.lower())
        else:
            swapped_list.append(i.upper())
    ## With map function
    # swapped_str = "".join(map(str, swapped_list))

    ##With list comprehension
    swapped_str = "".join(str(x) for x in swapped_list)

    return swapped_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)