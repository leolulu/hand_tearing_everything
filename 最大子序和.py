from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = {0: nums[0]}
        for i in range(1, len(nums)):
            if nums[i] + max_sum[i-1]> max_sum[i-1]:
                max_sum[i] = nums[i] + max_sum[i-1]
            else:
                max_sum[i] = max_sum[i-1]
        print(max_sum)
        return max(max_sum.values())


if __name__ == "__main__":
    s = Solution()
    print(
        s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    )
