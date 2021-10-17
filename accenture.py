# def f(m, n):
#     ans = 1
#     while(m-n >= 0):
#         (ans, m) = (ans*2, m-n)
#     return ans


# print(f(120, 13))

# def maximumSum(list1):
#     maxi = 0
#     # traversal
#     for x in list1:


#     return maxi


# # driver code
# list1 = [1, 2, 3]
# print(maximumSum(list1))

# def miniMaxSum(arr):
#     arr_sorted = sorted(arr)
#     return sum(arr_sorted[:4])


# print(miniMaxSum([1]))
# print(miniMaxSum([5,5,5,5,5]))


class Node:
    def __init__(self, value):
        self.children = []
        self.value = value

    def add_child(self, value):
        self.children.append(Node(value))

    def __repr__(self):
        classname = type(self).__name__
        return (f'{classname}({self.value!r}, {self.children})' if self.children else
                f'{classname}({self.value!r})')

    def print_stat(self):
        print(self.children)
        print(self.value)


class CountryTree:
    def __init__(self):
        self.continents = {}  # Dictionary mapping continents to countries.

    def add_country(self, country, parent=None):
        if not parent:  # Adding a continent?
            continent = country
            self.continents[continent] = Node(continent)
        else:  # Adding a country to a continent.
            continent = self.continents.get(parent, None)
            if not continent:
                raise KeyError(f'No continent named {parent} exists')
            continent.add_child(country)

    def get_country(self, parent):
        continent = self.continents.get(parent, None)
        if not continent:
            raise KeyError(f'No continent named {parent} exists')
        return continent.children


map = CountryTree()
map.add_country('A', None)
map.add_country('B', 'A')
map.add_country('C', 'A')
result = map.get_country('A')  # Should return China and Russia
result = ','.join(str(v) for v in result)
print(result)
