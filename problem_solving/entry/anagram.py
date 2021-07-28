"""
Anagram:
Given two strings, check whether two given strings are anagram of each other or not. 
An anagram of a string is another string that contains same characters, only the order 
of characters can be different. For example, “act” and “tac” are anagram of each other.
"""
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    if len(str1) != len(str2):
        return False

    str1 = str1.lower()
    str2 = str2.lower()

    # build 2 dict from all alphabet characters
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    dict1 = dict.fromkeys(list(alphabet), 0)
    dict2 = dict.fromkeys(list(alphabet), 0)

    # count the characters in the 2 strings 
    for i in range(len(str1)):
        dict1[str1[i]] += 1
        dict2[str2[i]] += 1

    print(dict1)
    print(dict2)
    # compare the 2 dicts
    return dict1 == dict2


if __name__ == "__main__":
    str1 = "practice makes perfect"
    str2 = "perfect makes practice"
    print(is_anagram(str1, str2))