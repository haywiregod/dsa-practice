# https://leetcode.com/problems/create-target-array-in-the-given-order/

def insertAtIndex(value, index, arr):

    arr.append(None)
    l = len(arr)
    for i in reversed(range(index, l)):
        arr[i] = arr[i-1]
    arr[index] = value


a = input("enter array: ")
a = [int(n) for n in a.split(" ")]

index = int(input("Enter index to insert on: "))
value = int(input("Enter value to be isnerted: "))

insertAtIndex(value, index, a)
print(a)
