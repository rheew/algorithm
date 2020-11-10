from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        
        ans = []
        if not nums or left >= len(nums): return [-1, -1]
        
        if nums[left] != target :
            ans.append(-1)
        else : ans.append(left)
        
        if nums[right - 1] != target :
            ans.append(-1)
        
        else : ans.append(right - 1)
            
        return ans
    