"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
"""

def main():
    to_sort_list = [3,5,1,9,7,2,10,4,8,6]
    print(to_sort_list)
    for i in range(len(to_sort_list), 1, -1):
        for j in range(1, i):
            if to_sort_list[j-1] > to_sort_list[j]:
                to_sort_list[j-1], to_sort_list[j] = to_sort_list[j], to_sort_list[j-1]
    print(to_sort_list)


if __name__ == "__main__":
    main()