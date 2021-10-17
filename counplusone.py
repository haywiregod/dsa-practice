def countElements(arr) -> int:
    """
    :type arr: List[int] - List of integers
    :rtype: int - Number of elements in arr satisfying the condition
    """

    arr2 = arr.copy()
    c = 0
    for a in arr:
        if a+1 in arr2:
            c += 1

    result = c

    return result


if __name__ == '__main__':
    line = input()
    components = line.strip().split()
    arr = [int(component) for component in components]

    print(countElements(arr))
