def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list)//2
    left_list = list[:mid]
    right_list = list[mid:]

    merge_sort(left_list)
    merge_sort(right_list)

    left_index = 0
    right_index = 0
    main_index = 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            list[main_index] = left_list[left_index]
            main_index += 1
            left_index += 1
        else:
            list[main_index] = right_list[right_index]
            main_index += 1
            right_index += 1

    while left_index < len(left_list):
        list[main_index] = left_list[left_index]
        main_index += 1
        left_index += 1

    while right_index < len(right_list):
        list[main_index] = right_list[right_index]
        main_index += 1
        right_index += 1

def main():
    list = [19, 56, 8, -6, -3, 27, -9, -29]
    print(list)
    merge_sort(list)
    print(list)


if __name__ == "__main__":
    main()