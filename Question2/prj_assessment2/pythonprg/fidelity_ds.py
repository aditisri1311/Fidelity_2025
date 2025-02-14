#sorting
def sort(arr):
    n = len(arr)
    for i in range(n - 1): #outer loop
        for j in range(n - i - 1): #inner loop iteration
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [6,9,1,19,8]
sort(arr)
print("Sorted list:", arr)
