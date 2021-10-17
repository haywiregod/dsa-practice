def insertionSort(arr):
    length = len(arr)
    for i in range(length-1):
        j = i+1
        while(j > 0):
            if(arr[j] < arr[j-1]):
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
                print('swapping..')
            else:
                print('breaking..')
                break
            j -= 1


a = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
(insertionSort(a))
print(a)
