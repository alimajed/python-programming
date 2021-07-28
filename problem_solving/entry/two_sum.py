def check_two_sum(nums, target):
    dct = {}
    for idx, num in enumerate(nums):
        print(num)
        print(dct)
        if num in dct:
            return [dct[num], idx]
        else:
            dct[target-num] = idx
    return None


if __name__ == "__main__":
    nums = [1,3,11,2,7]
    target = 9
    print(check_two_sum([1,3,11,2,7], 9))