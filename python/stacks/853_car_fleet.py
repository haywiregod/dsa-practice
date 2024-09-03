# https://leetcode.com/problems/car-fleet/
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True, key=lambda a: a[0])
        # print(f"Cars->{cars}")
        fleets = []
        for pos, spd in cars:
            timeToTarget = (target - pos) / spd
            # print(f"Fleets: {fleets}")
            fleets.append(timeToTarget)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
            # print(f"Fleets2: {fleets}")
        return len(fleets)


sol = Solution()

test_cases = [
    {
        "target": 12,
        "position": [10, 8, 0, 5, 3],
        "speed": [2, 4, 1, 1, 3],
    },
    {
        "target": 20,
        "position": [6, 2, 17],
        "speed": [3, 9, 2],
    },
    {
        "target": 10,
        "position": [8, 3, 7, 4, 6, 5],
        "speed": [4, 4, 4, 4, 4, 4],
    },
]

for index, test_case in enumerate(test_cases):
    print(f"Test: {index}: {sol.carFleet(**test_case)}")
