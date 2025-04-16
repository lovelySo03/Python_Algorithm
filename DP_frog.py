# 풀이 1

arr = [
    [0, 7, -3, -5],
    [-4, -2, 6, 5],
    [-9, -1, 0, 3],
    [2, 4, -6, 1]
]

dp = [[0] * 4 for _ in range(4)]

for i in range(1,4):
    dp[0][i] = dp[0][i - 1] + arr[0][i]
    dp[i][0] = dp[i - 1][0] + arr[i][0]

for i in range(1,len(arr)):
    for j in range(1,len(arr)):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]

print(dp[3][3])