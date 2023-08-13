class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a: int, b: int):
            return int(str(b)+str(a)) - int(str(a)+str(b))

        raw_result = ''.join(sorted([str(num) for num in nums], key=functools.cmp_to_key(comp)))
        i = 0
        while raw_result[i] == "0":
            i += 1
            if i == len(raw_result):
                return "0"

        return raw_result[i:] 