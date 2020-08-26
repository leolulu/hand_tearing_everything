from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0
        for idx2 in range(n):
            insert_num = nums2[idx2]

            while nums1[idx1] < insert_num and idx1 < m:
                idx1 += 1

            nums1.insert(idx1, insert_num)
            m += 1
            nums1.pop(-1)

        print(nums1)


if __name__ == "__main__":
    s = Solution()
    s.merge(nums1=[0,0,0], m=0, nums2=[2, 5, 6], n=3)
