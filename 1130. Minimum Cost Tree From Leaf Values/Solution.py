class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                for k in range(i, j):
                    root_val = max(arr[i : k + 1]) * max(arr[k + 1 : j + 1])
                    dp[i][j] = min(dp[i][j], root_val + dp[i][k] + dp[k + 1][j])
        return dp[0][n - 1]
