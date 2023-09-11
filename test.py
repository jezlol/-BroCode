import random

# Generate three lists of random numbers with varying lengths
nums1 = [random.randint(1, 100) for _ in range(50)]
nums2 = [random.randint(1, 100) for _ in range(75)]
nums3 = [random.randint(1, 100) for _ in range(100)]

# Store the arrays in a list
nums = [nums1, nums2, nums3]

# Define a function to find peak elements in an array
def Find_the_peak(array):
    n = len(array)
    peak_element = []

    # Handle the special case of an empty array
    if n == 0:
        return []

    # Handle the special case of an array with only one element
    if n == 1:
        return [0]

    # Check the first and last elements as potential peaks
    if array[0] > array[1]:
        peak_element.append(0)
    if array[n - 1] > array[n - 2]:
        peak_element.append(n - 1)

    # Loop through the elements from index 1 to n-2
    for i in range(1, n - 1):
        # Check if the current element is a peak by comparing with neighbors
        if array[i - 1] <= array[i] >= array[i + 1]:
            peak_element.append(i)

    return peak_element

# Iterate through the list of arrays
for i, array in enumerate(nums):
    # Call the Find_the_peak function for each array
    peak_elements = Find_the_peak(array)
    
    # Print the result for each array
    print(f"Peak element index of nums{i + 1}: {array} -> {peak_elements}")

# Additional code starts here

# Calculate the sum of peak elements in nums1, nums2, and nums3
sum_peak_elements_nums1 = sum(Find_the_peak(nums1))
sum_peak_elements_nums2 = sum(Find_the_peak(nums2))
sum_peak_elements_nums3 = sum(Find_the_peak(nums3))

print(f"Sum of peak elements in nums1: {sum_peak_elements_nums1}")
print(f"Sum of peak elements in nums2: {sum_peak_elements_nums2}")
print(f"Sum of peak elements in nums3: {sum_peak_elements_nums3}")

# Find the maximum value in each array
max_value_nums1 = max(nums1)
max_value_nums2 = max(nums2)
max_value_nums3 = max(nums3)

print(f"Maximum value in nums1: {max_value_nums1}")
print(f"Maximum value in nums2: {max_value_nums2}")
print(f"Maximum value in nums3: {max_value_nums3}")

# Calculate the average value in each array
average_nums1 = sum(nums1) / len(nums1)
average_nums2 = sum(nums2) / len(nums2)
average_nums3 = sum(nums3) / len(nums3)

print(f"Average value in nums1: {average_nums1}")
print(f"Average value in nums2: {average_nums2}")
print(f"Average value in nums3: {average_nums3}")

print("End of the program.")
