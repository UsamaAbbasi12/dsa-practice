def search(array, target_value):
    for index, value in enumerate(array):
        if target_value == value:
            print(index)


arr = [2, 5, 7, 9, 10, 34, 56, 78, 90]
target = 7

search(arr, target)
