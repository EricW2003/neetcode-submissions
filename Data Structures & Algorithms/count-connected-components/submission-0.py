class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dic = {i: [] for i in range(n)}
        for a,b in edges:
            dic[a].append(b)
            dic[b].append(a)
        
        states = set()

        def dfs(node):
            if node in states:
                return 
            states.add(node)

            for nei in dic[node]:
                dfs(nei)
        

 
        ans = 0
        for i in range(n):
            if i not in states:
                ans+=1
                dfs(i)

        return ans