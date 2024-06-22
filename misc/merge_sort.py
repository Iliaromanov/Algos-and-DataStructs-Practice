class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(l: int, r: int):
            if r == l + 1:
                return
            # not including r
            m = (l + r) // 2
            mergeSort(l, m)
            mergeSort(m, r)
            r_it = m
            l_it = l

            result = []
            while l_it < m or r_it < r:
                if l_it == m:
                    result.append(nums[r_it])
                    r_it+=1
                    continue

                if r_it == r :
                    result.append(nums[l_it])
                    l_it += 1
                    continue
                
                if nums[l_it] > nums[r_it]:
                    result.append(nums[r_it])
                    r_it += 1
                else:
                    result.append(nums[l_it])               
                    l_it += 1
            for i in range(l, r):
                nums[i] = result[i-l]
        mergeSort(0, len(nums))
        return nums