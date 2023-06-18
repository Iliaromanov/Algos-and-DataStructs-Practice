class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x : x[0]) # sort by starting time
        result = []
        i = 0
        while i < len(intervals):
            cur_s = intervals[i][0]
            cur_f = intervals[i][1]
            while i + 1 < len(intervals) and cur_f >= intervals[i+1][0]:
                i += 1
                cur_f = max(cur_f, intervals[i][1])

            result.append([cur_s, cur_f])
            i += 1

        return result