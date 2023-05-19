func merge(nums1 []int, m int, nums2 []int, n int)  {
    if n == 0 {
        return;
    }
    if m == 0 {
        for l, val := range nums2 {
            nums1[l] = val;
        }
    }
    ans := make([]int, len(nums1));
    i, j, k := 0, 0, 0;
    for i < m || j < n {
        if i >= m || (j<n && nums2[j] <= nums1[i]) {
            ans[k] = nums2[j];
            j++;
        } else if j >= n || nums1[i] < nums2[j] {
            ans[k] = nums1[i];
            i++;
        }
        k++;
    }
    for l, val := range ans {
        nums1[l] = val;
    }
}