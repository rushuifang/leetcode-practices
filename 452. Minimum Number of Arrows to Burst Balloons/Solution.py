 class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrow_count = 0
        popped_up_to = -inf
        for range_start, range_end in points:
            if range_start > popped_up_to:
                popped_up_to = range_end
                arrow_count += 1
        return arrow_count