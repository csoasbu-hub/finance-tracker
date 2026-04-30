class Solution:
    def pivotIndex(self, nums:]):
        value=sum(nums)
        left_side=0
        right_side=value-left_side
        for i in nums:
            if i >value:
                value=i
            if i+1==value:
        return value


        