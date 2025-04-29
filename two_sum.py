def two_sum(nums, target):
  """
  Finds two numbers in a list that add up to a target.

  Args:
    nums: A list of integers.
    target: The target sum.

  Returns:
    A list containing the indices of the two numbers that add up to the target,
    or None if no such pair is found.
  """
  num_map = {} # Dictionary to store number and its index

  for i, num in enumerate(nums):
    complement = target - num
    if complement in num_map:
      # Found the pair: the complement and the current number
      return [num_map[complement], i]
    # Store the current number and its index
    num_map[num] = i

  # No pair found
  return None

# Example usage:
# nums = [2, 7, 11, 15]
# target = 9
# result = two_sum(nums, target)
# print(f"Indices of the two numbers that sum to {target}: {result}") # Output: Indices of the two numbers that sum to 9: [0, 1]

# nums = [3, 2, 4]
# target = 6
# result = two_sum(nums, target)
# print(f"Indices of the two numbers that sum to {target}: {result}") # Output: Indices of the two numbers that sum to 6: [1, 2]

# nums = [3, 3]
# target = 6
# result = two_sum(nums, target)
# print(f"Indices of the two numbers that sum to {target}: {result}") # Output: Indices of the two numbers that sum to 6: [0, 1]

# nums = [1, 5, 9]
# target = 10
# result = two_sum(nums, target)
# print(f"Indices of the two numbers that sum to {target}: {result}") # Output: Indices of the two numbers that sum to 10: [0, 2]

