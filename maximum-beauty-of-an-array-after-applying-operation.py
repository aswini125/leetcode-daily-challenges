class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        # Step 1: Sort the array
        nums.sort()

        n = len(nums)
        max_beauty = 1  # Variable to track the maximum size of a valid subsequence

        # Step 2: Iterate through each element
        for i in range(n):
            # Find the upper bound index where nums[j] <= nums[i] + 2 * k
            ub = self.find(nums, nums[i] + 2 * k)
            # Update max_beauty with the size of the current valid subsequence
            max_beauty = max(max_beauty, ub - i + 1)
        
        return max_beauty  # Return the maximum valid subsequence size

    # Helper function to find the upper bound index where nums[j] <= val
    def find(self, nums: list[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1  # Stores the index of the last element <= val

        while l <= r:
            mid = l + (r - l) // 2  # Calculate mid-point
            if nums[mid] <= val:
                res = mid  # Update result and search in the right half
                l = mid + 1
            else:
                r = mid - 1  # Search in the left half
        
        return res  # Return the index of the last element <= val
