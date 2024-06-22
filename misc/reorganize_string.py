class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [[-count, char] for char, count in counts.items()]
        heapq.heapify(heap)

        print(heap)

        prev = None
        result = ""
        while heap:
            top = heapq.heappop(heap)
            result += top[1]
            top[0] += 1
            if prev is not None and prev[0] != 0:
                heapq.heappush(heap, prev)
            prev = top

        if prev is not None and prev[0] != 0:
            return ""
        
        return result
