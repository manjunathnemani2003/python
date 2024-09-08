def count_partitions(N):
    # Initialize the dp array with zeros
    dp = [0] * (N + 1)
    print(dp)
    dp[0] = 1
    print(dp)# There is one way to partition 0

    for i in range(1, N + 1):
        for j in range(i, N + 1):
            dp[j] += dp[j - i]
            print(dp)

    return dp[N]

# Example usage:
N=int(input("enter the number: "))
if N<=0:
  print("invalid input")
else:
  print(count_partitions(N))  # Output: 5
