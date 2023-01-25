#include <utility>
#include <vector>

class Solution {
public:
    void dfs(std::vector<std::vector<int>>& image, int sr, int sc, int new_color) {
        int old_color = image[sr][sc];
        image[sr][sc] = new_color;

        std::vector<std::pair<int, int>> trans = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        for (auto &p : trans) {
            int i = p.first;
            int j = p.second;
            int new_r = sr + i;
            int new_c = sc + j;
            if (0 <= new_r and new_r < image.size() and 0 <= new_c and new_c < image[0].size() 
                and image[new_r][new_c] == old_color) {
                dfs(image, new_r, new_c, new_color);
            }
        }

    }

    std::vector<std::vector<int>> floodFill(std::vector<std::vector<int>>& image, int sr, int sc, int color) {
        if (image[sr][sc] != color) {
            dfs(image, sr, sc, color);
        }

        return image;
    }
};