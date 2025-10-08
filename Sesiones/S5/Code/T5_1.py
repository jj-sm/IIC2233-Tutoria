# Import the 'eq' function from the 'operator' module
from operator import eq

def igual(a, b):
    return a == b

# Define a function 'count_same_pair' that takes two lists as input and returns the number of pairs with equal elements
def count_same_pair(nums1, nums2):
    # Use the 'map' function with 'eq' to create a list of True/False values for corresponding elements in 'nums1' and 'nums2'
    # Sum the True values to get the count of pairs with equal elements
    result = sum(map(eq, nums1, nums2))
    # Return the result
    return result

# Define two lists 'nums1' and 'nums2'
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]

# Print the original lists
print("Original lists:")
print(nums1)
print(nums2)

# Print a newline for better readability
print("\n")

# Print the number of pairs with equal elements in the two lists
print("Number of same pair of the said two given lists:")
print(count_same_pair(nums1, nums2))
