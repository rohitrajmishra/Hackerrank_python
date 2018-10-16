if __name__ == '__main__':
    s = input()

    bool_isalnum = False
    bool_isalpha = False
    bool_isdigit = False
    bool_islower = False
    bool_isupper = False

    for i in s:
        if i.isalnum():
            bool_isalnum = True
        if i.isalpha():
            bool_isalpha = True
        if i.isdigit():
            bool_isdigit = True
        if i.islower():
            bool_islower = True
        if i.isupper():
            bool_isupper = True

    # Print flag values
    print(bool_isalnum)
    print(bool_isalpha)
    print(bool_isdigit)
    print(bool_islower)
    print(bool_isupper)