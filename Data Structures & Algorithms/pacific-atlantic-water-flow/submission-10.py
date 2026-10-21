class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_visited = set()

        n, m = len(heights), len(heights[0])

        for i in range(n):
            pacific_visited.add((i,0))
        for j in range(m):
            pacific_visited.add((0,j))
        
        q = deque(pacific_visited)

        while q:
            for _ in range(len(q)):
                i,j = q.popleft()

                nei = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                for k,l in nei:
                    if k<n and k>=0 and l<m and l>=0 and heights[k][l]>=heights[i][j] and (k,l) not in pacific_visited:
                        pacific_visited.add((k,l))
                        q.append((k,l))
        

        atlantic_visited = set()


        for i in range(n):
            atlantic_visited.add((i,m-1))
        for j in range(m):
            atlantic_visited.add((n-1,j))
        
        q = deque(atlantic_visited)

        while q:
            for _ in range(len(q)):
                i,j = q.popleft()

                nei = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                for k,l in nei:
                    if k<n and k>=0 and l<m and l>=0 and heights[k][l]>=heights[i][j] and (k,l) not in atlantic_visited:
                        atlantic_visited.add((k,l))
                        q.append((k,l))

        ans = []

        for i in range(n):
            for j in range(m):
                if (i,j) in pacific_visited and (i,j) in atlantic_visited:
                    ans.append([i,j])

        return ans
                