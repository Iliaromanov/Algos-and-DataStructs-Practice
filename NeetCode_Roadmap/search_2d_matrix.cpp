class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // vertical binary search
        int bottom = 0;
        int top = matrix.size() - 1;
        while (bottom <= top)
        {
            int m = bottom + (top - bottom) / 2;

            if (matrix[m][0] <= target && target <= matrix[m].back())
            {
                bottom = m;
                break;
            }  
            else if (target < matrix[m][0])
                top = m - 1;
            else // target > matrix[m].back()
                bottom = m + 1;
        } 

        // no suitable row found 
        if (bottom >= matrix.size() || target < matrix[bottom][0] || target > matrix[bottom].back())
            return false;

        // horizontal binary search
        int l = 0;
        int r = matrix[0].size() - 1;
        while (l <= r)
        {
            int m = l + (r - l) / 2;

            if (matrix[bottom][m] == target)
                return true;
            else if (target < matrix[bottom][m])
                r = m - 1;
            else // target > matrix[bottom][m]
                l = m + 1;
        }

        return false;
    }
};
