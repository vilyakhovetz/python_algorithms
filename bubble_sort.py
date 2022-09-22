def bubble_sort(array, reverse=False):
    """
    Function for sorting the list (in ascending order by default).
    The reverse flag can be set to sort in descending order.
    """
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if reverse:
                if array[j] < array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True
            else:
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    test_array = [7, 85, 49, 22, 85, 93, 1, 89, 48, 80]
    print(test_array)
    bubble_sort(test_array)
    print(f'Ascending order: {test_array}')
    bubble_sort(test_array, reverse=True)
    print(f'Descending order: {test_array}')
