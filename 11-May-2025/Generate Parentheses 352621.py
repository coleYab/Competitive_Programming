# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def valid(path):
            st = []
            for i in path:
                if i == ')' and not st:
                    return False
                elif i == ')':
                    st.pop()
                    continue

                st.append(i)

            # print(st, path)
            return len(st) == 0
    
        def dfs(path):
            if len(path) == n * 2:
                if valid(path):
                    ans.append("".join(path))
                # print(path)
                return

            path.append('(')
            dfs(path)
            path.pop()
            path.append(')')
            dfs(path)
            path.pop()

        dfs([])
        # print("valid ? ", valid(['(', ')', '(', ')', '(', ')']))
        return ans