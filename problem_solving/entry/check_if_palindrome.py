import string


def is_palindrome(s):
    # convert to lower
    s = s.lower()
    # remove punctuation
    s = s.translate(s.maketrans('','',string.punctuation))
    # remove spaces
    s = s.replace(" ", "")

    return s == s[::-1]


if __name__ == "__main__":
    str1 = "race car"
    str2 = "Dammit I'm mad."
    str3 = "computer"

    print(is_palindrome(str1))
    print(is_palindrome(str2))
    print(is_palindrome(str3))