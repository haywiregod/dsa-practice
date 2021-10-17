def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1 1 1 1 1 1 2 2 1 1
    hashArr = [0]*101
    for i in nums:
        hashArr[i] += 1

    c = 0
    for i in range(len(hashArr)):
        print(f"hash[{i}]={hashArr[i]}")
        if hashArr[i] > 1:
            np = getNumOfPairs(hashArr[i])
            print(f"np  for {i} = {np}")
            c += np
            print(f"c is now {c}")
    return c


def getFactorial(num):
    f = 1
    for i in range(1, num+1):
        f = f*i
    return f


def getNumOfPairs(num):

    return getFactorial(num)//(getFactorial(num-2)*2)


a = input("enter array")
a = [int(n) for n in a.split(" ")]
print("good pairs: ", numIdenticalPairs(a))
