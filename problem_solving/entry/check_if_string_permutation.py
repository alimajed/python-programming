"""
A Permutation of a string is another string that contains same characters, only the order of characters can be different.
"""

def is_permutation(str1, str2):
    # remove spaces from strings
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    if len(str1) != len(str2):
        return False

    for char in str1:
        if char in str2:
            str2 = str2.replace(char, "")

    return len(str2) == 0


if __name__ == "__main__":
    str1 = "driving"
    str2 = "drivign"
    str3 = "criving"

    print(is_permutation(str1, str2))
    print(is_permutation(str2, str3))