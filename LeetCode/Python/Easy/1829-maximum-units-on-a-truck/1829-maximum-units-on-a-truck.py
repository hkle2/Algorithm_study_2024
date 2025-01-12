class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sortedBoxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        answer = 0
        for numBoxes, unit in sortedBoxTypes:
            if truckSize > numBoxes:
                answer += numBoxes * unit
                truckSize -= numBoxes
            else:
                answer += truckSize * unit
                break
        return answer

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer = 0
        boxTypes.sort(key=lambda x: -x[1])
        for i in range(len(boxTypes)):
            if truckSize >= boxTypes[i][0]:
                answer += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
            else:
                answer += truckSize * boxTypes[i][1]
                break
        return answer

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer = 0
        boxTypes.sort(key=lambda x: -x[1])
        for i, [num, unit] in enumerate(boxTypes):
            if truckSize >= num:
                answer += num * unit
                truckSize -= num
            else:
                answer += truckSize * unit
                break
        return answer