# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:
    def __init__(self, n: int):
        self.heap = list(range(1, n + 1))
        heapify(self.heap)        

    def reserve(self) -> int:
        return heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.heap, seatNumber)


# Is you kidding