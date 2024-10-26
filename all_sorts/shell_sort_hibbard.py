def shell_sort_hibbard(arr):

    n = len(arr)
    gap = 1
    while gap < n // 3:
        gap = 2 * gap + 1

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr