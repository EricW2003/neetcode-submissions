class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = {i: [] for i in range(n)}
        for a,b in edges:
            dic[a].append(b)
            dic[b].append(a)
        
        states = [-1]*n

        def dfs(node, preceding_node=None):
            if states[node]==0:
                return False
            if states[node]==1:
                return True
            
            states[node] = 0

            for nei in dic[node]:
                if preceding_node is None or preceding_node!=nei:
                        if not dfs(nei,node):
                            return False    

            states[node] = 1

            return True
        
        if not dfs(0):
            return False 
            
        return True and n==sum(states)

# def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
#         dic = {i: [] for i in range(numCourses)}

#         for a,b in prerequisites:
#             dic[a].append(b)

#         ans = []

#         # 0 not seen, 1 under investigation, 2 done
#         states = [0]*numCourses
        
#         def backtracking(i):
#             if states[i]==1:    
#                 return False
#             if states[i]==2:
#                 return True

#             states[i]=1
#             for nei in dic[i]:
#                 if not backtracking(nei):
#                     return False
            
#             states[i] = 2
#             ans.append(i)
#             return True

#         for i in range(numCourses):
#             if not backtracking(i):
#                 return []

#         return ans