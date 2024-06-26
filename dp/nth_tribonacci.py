def tribonacci(n: int) -> int:
    # O(1) space
    dp = [0,1,1] 
    for i in range(3,n+1):
        dp[i%3] = dp[(i+1)%3]+dp[(i+2)%3]+dp[(i+3)%3]
    return dp[n%3]