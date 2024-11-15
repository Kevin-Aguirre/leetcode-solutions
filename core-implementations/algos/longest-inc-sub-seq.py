def longest_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return 0
    # Initialize the DP array where dp[i] represents the length of LIS ending at index i
    dp = [1] * n  # Every element is an increasing subsequence of length 1

    # Build the dp array
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # The length of the longest increasing subsequence will be the maximum value in dp\
    return max(dp)

# Example usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Length of monotonically increasing subsequence:", longest_increasing_subsequence(arr))
