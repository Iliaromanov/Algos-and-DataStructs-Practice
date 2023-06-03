class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        mask = 1 << 31
        for i in range(32):
          if mask & n:
            res |= (1 << i)
          mask >>= 1
        return res