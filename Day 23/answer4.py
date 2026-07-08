#Explain in your own words:

# Why do we reset current_sum to 0 when it becomes negative?

# No code.

# explanation:

# If current sum is negative, adding it to the next element only makes the next sum smaller.

# Example:

# current = -2

# next = -3

# -2 + (-3) = -5

# Since

# -3 > -5

# it is better to start from -3.

# ✅ This is exactly the intuition behind Kadane's Algorithm.

# Very well explained.