def string_compression(string):
    com_str = ""

    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            com_str += f"{string[i]}{count}"
            count = 1
    # catch out with last character
    com_str += f"{string[i]}{count}"
    return com_str

if __name__ == "__main__":
    input_str_test_1 = "aabcccccaaa"
    input_str_test_2 = "aaaaaabbccbcaabb"

    print(string_compression(input_str_test_1))
    print(string_compression(input_str_test_2))
    print(bin(5))