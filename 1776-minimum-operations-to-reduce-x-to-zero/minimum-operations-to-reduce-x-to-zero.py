class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        left = 0
        window_sum = 0
        max_len = -1
        
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum > target and left <= right:
                window_sum -= nums[left]
                left += 1
            if window_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len if max_len != -1 else -1