def main():
    list = [-29, -16, -15, -9, -6, -3, 8, 10, 17, 19, 27, 47, 54, 56, 60]
    # print(list)
    element = -9
    start = 0
    end = len(list)-1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == element:
            print(f"element found {element} at index {mid}")
            break
        elif element < list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    


if __name__ == "__main__":
    main()