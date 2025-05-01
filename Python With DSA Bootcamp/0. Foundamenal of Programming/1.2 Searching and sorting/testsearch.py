def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        previous = i - 1

        while previous >= 0 and arr[previous] > current:
            arr[previous + 1] = arr[previous]
            previous = previous - 1

        arr[previous + 1] = current
        print(arr)
    return arr


print(
    insertion_sort(
        [
            4,
            1,
            5,
            2,
            3,
        ]
    )
)
