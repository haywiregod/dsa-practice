def nextGreatestChar(charList, target):
    start = 0
    end = len(charList)-1
    while(start <= end):
        mid = int(start + (end-start)/2)
        print("mid at", mid)
        if(charList[mid] > target):
            end = mid - 1
            print("end at", end)
        else:
            start = mid+1
            print("start at", start)
    return charList[start % len(charList)]


def bs(intList, target, start, end):
    ans = -1
    while(start <= end):
        mid = int(start + (end-start)/2)
        if target == intList[mid]:
            return mid
        elif intList[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return ans

# 0 1 2 3 4 5 6 7 8 9 10
# 0 1
# 2 4
# 5 13


def inifinteArrayBS(intList, target):
    ans = -1
    start = 0
    end = 1
    tries = 0
    while(start <= end and tries < 1000):
        tries += 1
        print(f'start {start} end {end}')
        print(f'boxSize {int((end+start)/2)}')
        ans = bs(intList, target, start, end)
        if(ans == -1):
            # target not found, increase window

            start = end + 1
            end = 2*(end)+start
        else:
            return ans
    return ans

# 0 1 2 3 4 5 3 2 0
# 0 1 2 3 4 5 6 7 8
# m 4, s 5, e 8
# m 6,


def findPeak(intList):
    start = 0
    end = len(intList)-1
    ans = -1
    while(start != end):
        mid = int((start+end)/2)
        print(f"start {intList[start]} end {intList[end]} mid {intList[mid]}")

        if intList[(mid+1)] >= intList[mid]:
            # in incresing part
            start = mid+1
        else:
            # start = start+1
            end = mid
        ans = end
        print(f"ans {ans}")
    return ans


a = [3, 4, 5, 99, 100, 110, 76, 65, 54, 1]
# =  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
# print(findPeak(a))
# 8 9 10 11 12 13 14 15 0 1 2 3 4 5 6 7


def findPivot(arr):
    s = 0
    e = len(arr)-1
    if (e == 0):
        return 0
    while(s <= e):
        print(f's {s} e {e}')
        m = int((s+(e-s)/2))
        print(f'm {m}')
        if e == m:
            return m
        if e > m and arr[m] > arr[m+1]:
            # pivot found
            print('pivot found at m', arr[m])
            return abs(m)
        if s <= m and arr[m] < arr[m-1]:
            print('pivot found at m-1', m-1, arr[m-1])
            return abs(m-1)
        if arr[m] <= arr[s]:
            print(f'pivot not found, compared {arr[m]} <= {arr[s]}')
            e = abs(m-1)
            print(f'set e = {e}')
        else:
            print(f'pivot not found, else compared {arr[m]} >= {arr[s]}')
            s = abs(m+1)
            print(f'set s = {s}')
        print(f'-----------------')
    print('loop ended')
    return len(arr)-1


# 1 2 3 4 5 6 7 8
a = [5, 6, 7, 8, 8, 1, 1, 2, 3, 3, 4]


def findTarget(arr, target):
    pivot = findPivot(arr)
    print("pivot is", pivot)
    if target == arr[pivot]:
        return pivot
    a = -1
    e = len(arr)-1
    s = 0
    if target >= arr[s]:
        s = 0
        e = pivot-1
        a = bs(arr, target, s, e)
    else:
        s = pivot+1
        a = bs(arr, target, s, e)
    return a


# print(findTarget(a, 1))
print(findTarget(a, 3))
# solve for duplicates too

# 1,2,3,4,5,6,7,8,9
# 6,7,8,9,1,2,3,4,5
# 4,5,6,7,8,9,1,2,3
