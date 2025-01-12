class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        answer = 0
        for seat, student in zip(seats, students):
            answer += abs(seat - student)
        return answer

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        answer = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            answer += abs(seats[i] - students[i])
        return answer