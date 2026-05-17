def binary_search(arr: list, target: int) -> int:
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    guess = arr[mid]

    while low<=high:
        if guess == target:
            return mid
        elif guess>target:
            high=mid-1

        else:
            low = mid+1

    return -1


my_list = [1,3,5,7,9,11,13,15]
target_value=7

result = binary_search(my_list,target_value)
