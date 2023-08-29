class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i >= 1:
            par_i = (i - 1) // 2
            if self.heap[par_i] < self.heap[i]:
                self.heap[par_i], self.heap[i] = self.heap[i], self.heap[par_i]
            else:
                break
            i = par_i
    
    def popMax(self):
        cur_max = self.heap[0]
        if len(self.heap) == 1:
            return cur_max
        self.heap[0] = self.heap.pop()
        i = 0
        while 2 * i + 1 < len(self.heap):
            max_i = 2 * i + 1
            if 2 * i + 2 < len(self.heap) and self.heap[2*i + 2] > self.heap[max_i]:
                max_i = 2*i + 2
            if self.heap[max_i] > self.heap[i]:
                self.heap[max_i], self.heap[i] = self.heap[i], self.heap[max_i]
            else:
                break
            i = max_i

        return cur_max


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = MaxHeap()
        for num in nums:
            h.insert(num)
        kth_max = 0
        for _ in range(k):
            kth_max = h.popMax()
            print("kth max: ", kth_max)

        return kth_max
