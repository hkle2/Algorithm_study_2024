class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer = 0
        boxTypes.sort(key=lambda x: -x[1])
        for i in range(len(boxTypes)):
            if truckSize > 0:
                if truckSize >= boxTypes[i][0]:
                    answer += boxTypes[i][0] * boxTypes[i][1]
                    truckSize -= boxTypes[i][0]
                else:
                    answer += truckSize * boxTypes[i][1]
                    truckSize -= truckSize
        return answer