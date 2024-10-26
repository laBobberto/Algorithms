def selection_sort(arr):
    """
    Сортировка выбором
    """
    for i in range(len(arr)):

        min_element_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_element_index]:
                min_element_index = j

        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]
