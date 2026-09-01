class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        array = []
        def inserter(array, val):
            if array == []:
                array.append(val)
            elif val <array[0]:
                array.insert(0, val)
            elif val > array[-1]:
                array.append(val)
            else:     
                a = 0

                b = len(array)

                # loop invariant array[a] <= val <= array[b]
                while 1 < b - a:
                    mid = (a+b)//2
                    if array[mid] <= val:
                        a = mid
                    
                    else:
                        b = mid 
                array.insert(a+1, val)
        for val in nums:
            inserter(array,val)
        return array