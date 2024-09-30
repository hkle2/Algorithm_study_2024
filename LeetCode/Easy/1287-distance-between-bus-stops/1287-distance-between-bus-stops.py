class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # 역방향 거리 = 전체 둘레 - 정방향 거리
        total_distance = sum(distance)
        if start <= destination:
            forward_distance = sum(distance[start:destination])
        else:
            forward_distance = sum(distance[start:]) + sum(distance[:destination])
        backward_distance = total_distance - forward_distance
        return min(forward_distance, backward_distance)

# class Solution:
#     def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
#         if start < destination:
#             return min(sum(distance) - sum(distance[start:destination]), sum(distance[start:destination]))
#         return min(sum(distance) - sum(distance[destination:start]), sum(distance[destination:start]))