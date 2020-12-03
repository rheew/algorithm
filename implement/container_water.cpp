#include <algorithm>

class Solution {
public:
    int maxArea(vector<int>& height) {
        int N = height.size();
        int end = N - 1;
        int start = 0;
        int ans = 0;
        
        while(start < end) {
            int bottom = end - start;
            
            if (height[start] < height[end]) {
                ans = max(ans, height[start] * (bottom));
                start++;
            }
            else {
                ans = max(ans, height[end] * (bottom));
                end--;
            }
        }
        
        return ans;
    }
};