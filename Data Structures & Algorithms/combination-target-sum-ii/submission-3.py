class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, curSum):
            if curSum == target:
                res.append(list(cur))
                return
            if curSum > target:
                return

            for j in range(i, len(candidates)):
                # Skip duplicate elements at the same decision level
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
            
                cur.append(candidates[j])
                dfs(j + 1, cur, candidates[j] + curSum)
                cur.pop()
        dfs(0, [], 0)

        return res