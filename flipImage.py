def reverseAndFlipArray(arr):
    l = len(arr)
    s = 0
    e = l-1
    while s <= e:
        if arr[s] == 0:
            arr[s] = 1
        else:
            arr[s] = 0
        if e != s:
            if arr[e] == 0:
                arr[e] = 1
            else:
                arr[e] = 0
        if arr[s] != arr[e]:
            temp = arr[s]
            arr[s] = arr[e]
            arr[e] = temp

        s += 1
        e -= 1


a = [1, 1, 1, 0]

reverseAndFlipArray(a)
print(a)
