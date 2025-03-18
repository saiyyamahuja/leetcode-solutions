class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        # need to traverse through s
        # backtrack each case of  start index and then +,*,-
        # need empty array ofcourse
        # need curidx = i
        # need the str path to append to the arr if my --> cur_num == target
        # need the prevNum access for multiplication
        # 1 2 3 4 5 --> 1 + 2 + 3 + 4 * 5
        #               ^ ^ ^ ^ ^ ^ ^ == 10 but we wanna do 4*5 so ---
        # just do 1 + 2 + 3 + 4 + (- 4) + (4 * 5)
        # return ans
        
        res = []

        def dfs(i, path, cur_num, prevNum):
            if i == len(s):
                if cur_num == target:
                    res.append(path)
                return
            
            for j in range(i, len(s)):
                # starting with zero?
                if j > i and s[i] == '0':
                    break
                num = int(s[i:j+1])

                # if cur index is 0 then simple add that number
                if i == 0:
                    dfs(j + 1, path + str(num), cur_num + num, num)
                else:
                    dfs(j + 1, path + "+" + str(num), cur_num + num, num)
                    dfs(j + 1, path + "-" + str(num), cur_num - num, -num)
                    dfs(j + 1, path + "*" + str(num), cur_num - prevNum + prevNum * num, prevNum * num)
        
        dfs(0, "", 0, 0)
        return res
        