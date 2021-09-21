"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
In fact insertion sort is kind of the opposite of the bubble ssince we start from the left
"""

def main():
    to_sort_list = [3,5,1,9,7,2,10,4,8,6]
    print(to_sort_list)
    for i in range(1, len(to_sort_list)):
        for j in range(i, 0, -1):
            if to_sort_list[j] < to_sort_list[j-1]:
                to_sort_list[j], to_sort_list[j-1] = to_sort_list[j-1], to_sort_list[j]
            else:
                break
    print(to_sort_list)


if __name__ == "__main__":
    main()