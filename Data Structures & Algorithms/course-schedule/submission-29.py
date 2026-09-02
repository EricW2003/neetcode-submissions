class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            dic[a].append(b)
        def backtracking(i):
          if i in path:
            return False
          path.add(i)
          while dic[i]!=[]:
              nei = dic[i].pop()
              if not backtracking(nei):
                return False
          path.remove(i)
          return True

        for i in range(numCourses):
          path = set()
          if not backtracking(i):
            return False
        return True


        
        
