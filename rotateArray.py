# 1 2 3 4 5 6 7 8 9 10 11

def rotate(nums, k):
    r = []
    l = len(nums)
    for i in range(k+1, l):
        r.append(nums[i])
    for i in range(0, k+1):
        r.append(nums[i])
    return r


if __name__ == '__main__':
    line = input()
    components = line.strip().split()
    nums = [int(component) for component in components]

    k = int(input())

    nums = rotate(nums, k)

    print(nums)

# 11 -3 = 8
