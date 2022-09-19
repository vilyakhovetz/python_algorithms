def binary_search(array, value):
    """
    Function for finding an element in a sorted array using array splitting in half.
    Returns first index of value.
    Raises ValueError if the value is not present.
    """
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        guess = array[mid]
        if guess == value:
            return mid
        if guess > value:
            end = mid - 1
        else:
            start = mid + 1
    raise ValueError(f'{value} is not in list')


if __name__ == '__main__':
    test_array = [5, 18, 19, 24, 40, 49, 49, 56, 62, 97]
    test_value = 49
    print(test_array)
    print(f'Value {test_value} is present at index {binary_search(test_array, test_value)}')
