def sort(arr):
    i = 0
    while(i < len(arr)):
        if(arr[arr[i]-1] != arr[i]):
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
        else:
            i += 1


def findMissingNumber(arr):
    i = 0
    length = len(arr)
    while(i < length):
        if(arr[i] < length and arr[arr[i]] != arr[i]):
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        else:
            i += 1

    i = 0
    while(i < length):
        if arr[i] != i:
            return i
        i += 1
    return length


def findMissingNumbers(arr):
    i = 0
    length = len(arr)
    while(i < length):
        if(arr[i] < length and arr[arr[i]] != arr[i]):
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        else:
            i += 1

    i = 0
    missingNumbers = []
    print(arr)
    while(i < length):
        if arr[i] != i+1:
            missingNumbers.append(i)

        i += 1
    missingNumbers.append(i)
    return missingNumbers


a = [0, 8, 6, 7]

print(findMissingNumbers(a))
