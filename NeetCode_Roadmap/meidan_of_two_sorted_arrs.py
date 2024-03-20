class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # run bin search on smaller of two arrs -> nums1
        if len(nums1) > len(nums2): 
            nums1, nums2 = nums2, nums1
        
        len_total = len(nums1) + len(nums2)
        k = len_total // 2

        l, r = 0, len(nums1) - 1
        while True:
            mid1 = l + (r - l) // 2
            mid2 = k - (mid1 + 1) - 1

            nums1_left = nums1[mid1] if mid1 >= 0 else float("-inf")
            nums2_left = nums2[mid2] if mid2 >= 0 else float("-inf")
            nums1_right = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float("inf")
            nums2_right = nums2[mid2 + 1] if mid2 + 1 < len(nums2) else float("inf")

            if nums2_left > nums1_right:
                l = mid1 + 1
                continue
            
            if nums1_left > nums2_right:
                r = mid1 - 1
                continue

            # return result
            if len_total % 2 == 0:
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            return min(nums1_right, nums2_right)

        return -1
