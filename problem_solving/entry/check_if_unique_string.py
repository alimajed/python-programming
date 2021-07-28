def check_if_string_unique(string):
    # chars = []
    # for char in string:
    #     if char in chars:
    #         return False
    #     chars.append(char)
    # return True

    return len(string) == len(set(string))


if __name__ == "__main__":
    str1 = "unique"
    str2 = "bear"

    print(check_if_string_unique(str1))
    print(check_if_string_unique(str2))