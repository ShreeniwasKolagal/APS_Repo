def knapsack_dp(values, weights, capacity):
    """
    values: list of item values (length n)
    weights: list of item weights (length n)
    capacity: integer maximum weight capacity
    Returns the maximum total value achievable.
    """
    n = len(values)
    # dp[i][w] = max value using first i items with total weight ≤ w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        v = values[i - 1]
        wt = weights[i - 1]
        for w in range(capacity + 1):
            # either skip item i or take it (if it fits)
            dp[i][w] = dp[i - 1][w]
            if wt <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - wt] + v)

    return dp[n][capacity]


# Example usage:
vals = [60, 100, 120]
wt = [10, 20, 30]
cap = 50
print(knapsack_dp(vals, wt, cap))  # Output: 220
