class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # duplicate, missing = None, None

        # # Check for duplicate
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         duplicate = nums[i]

        # # Check for missing
        # for i in range(1, len(nums) + 1):
        #     if i not in nums:
        #         missing = i
        #         break

        # return [duplicate, missing]

            n = len(nums)
            duplicate, missing = None, None
            seen = set()

            for num in nums:
                if num not in seen:
                    seen.add(num)
                else:
                    duplicate = num

            # The missing number is the one that's not in the seen set
            missing = sum(range(1,n+1)) - sum(seen)

            return [duplicate,missing]           
