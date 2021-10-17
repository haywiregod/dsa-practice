class Solution:
    def addToArrayForm(self, num, k):
        i = len(num)-1
        a = []
        while(i >= 0 or k > 0):
            if(i >= 0):
                num[i] = (num[i]+k) % 10
                k = (num[i]+k)//10
            else:
                num.insert(0, k % 10)
                k = k//10
            i -= 1
        return num


a = input("enter array: ")
a = [int(n) for n in a.split(" ")]
k = int(input("Enter num to be added: "))

s = Solution()
print(s.addToArrayForm(a, k))
# 999
# 2 7 4
# 2 7 3
#   2 8 3
# 2 7 3
#   3 7 3
# 3 7 3
# 2 7 3
# 1 2 7 3
