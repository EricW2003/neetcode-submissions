class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n_fleet = 1
        arr = [(pos, v) for pos, v in zip(position,speed)]
        arr.sort()
        time_taken = (target-arr[-1][0])/arr[-1][1]

        for i in range(len(position)-2,-1,-1):
            pos = arr[i][0]
            v = arr[i][1]
            t = (target-pos)/v
            if t > time_taken:
                time_taken = t
                n_fleet += 1
        return n_fleet