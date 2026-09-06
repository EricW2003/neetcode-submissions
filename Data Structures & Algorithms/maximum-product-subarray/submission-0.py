
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = [0]*len(nums)
        # ans[i] = (max prod starting from ans[i], min prod starting from ans[i] )

        ans[-1] = (nums[-1],nums[-1])

        # nums = [2,4,-3,5] 
        # ans = [ (8,-120)    (4, -60)   (-3, -15) (5,5)]
        # ans[i] f(ans[i+1])
        max_val = ans[-1][0]
        for i in range(len(nums)-2,-1,-1):
            max_element, min_element = ans[i+1]

            num = nums[i]
            if num==0:
                ans[i] = (0,0)
                max_val = max(max_val, ans[i][0])
            elif num>0:
                if max_element>0:
                    max_i = max_element*num
                else:
                    max_i = num
                if min_element<0:
                    min_i = num*min_element
                else:
                    min_i = num
                ans[i] = (max_i,min_i)
                max_val = max(max_val, max_i)
            else:
                if min_element<0:
                    max_i = min_element*num
                else:
                    max_i = num
                if max_element>0:
                    min_i = num*max_element
                else:
                    min_i = num
                ans[i] = (max_i,min_i)
                max_val = max(max_val, max_i)
        return max_val

