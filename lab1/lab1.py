def binary_search(arr: list, target: int) -> int | str:
    """Выполняет бинарный поиск элемента в отсортированном массиве.

    Args:
        arr (list): Отсортированный список элементов для поиска.
        target (int): Искомое значение.

    Returns:
        int: Индекс найденного элемента в массиве или -1, если элемент не найден.
    """
    low = 0
    high = len(arr) - 1

    if(len(arr)) == 0:
        return "Введите ненулевой список"

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


my_list = [1,3,5,7,9,11,13,15]
target_value=7

result = binary_search(my_list,target_value)
print(result)
