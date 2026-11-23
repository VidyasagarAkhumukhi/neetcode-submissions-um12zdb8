class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        candidates.sort()

        def dfs(i, curr, total):
            if target == total:
                res.append(curr.copy())
                return

            if total > target or i >= len(candidates):
                return
        
            # including candidates[i] in the curr combination  
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            # not including candidates[i] in the curr combination  
            curr.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)


        dfs(0, curr, 0)
        return res    