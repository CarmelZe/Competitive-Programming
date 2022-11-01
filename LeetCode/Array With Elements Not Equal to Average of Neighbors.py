class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        sol = []

        x, y = 0, len(nums)-1
        while len(sol) != len(nums):
            sol.append(nums[x])
            x += 1

            if x <= y:
                sol.append(nums[y])
                y -= 1
        return sol