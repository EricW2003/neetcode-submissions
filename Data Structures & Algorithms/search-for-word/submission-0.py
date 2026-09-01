class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m = len(board[0])
        list_bool = [False]
        def aux(index,curr_position, visited):
            if index == len(word)-1:
                list_bool[0] = True
                return

            i , j = curr_position

            if i+1<=n-1 and (i+1,j) not in visited and word[index+1]==board[i+1][j]:
                a = visited.copy()
                a.add((i+1,j))
                aux(index+1,(i+1,j),a)

            if i-1>-1 and (i-1,j) not in visited and word[index+1]==board[i-1][j]:
                a = visited.copy()
                a.add((i-1,j))
                aux(index+1,(i-1,j),a)

            if j+1<=m-1 and (i,j+1) not in visited and word[index+1]==board[i][j+1]:
                a = visited.copy()
                a.add((i,j+1))
                aux(index+1,(i,j+1),a)
            
            if j-1>-1 and (i,j-1) not in visited and word[index+1]==board[i][j-1]:
                a = visited.copy()
                a.add((i,j-1))
                aux(index+1,(i,j-1),a)


        first_letter = word[0]
        for i in range(n):
            for j in range(m):
                if board[i][j] == first_letter:
                    aux(0,(i,j),set([(i,j)]))
                    if list_bool[0]:
                        return True
        return False

