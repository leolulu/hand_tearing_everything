from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        pass_min = prices[0]
        max_reward = [0]
        for i in prices[1:]:
            if i < pass_min:
                pass_min = i
            max_reward.append(i-pass_min)
        return max(max_reward)


if __name__ == "__main__":
    s = Solution()
    print(
        s.maxProfit([7, 6, 4, 3, 1])
    )
