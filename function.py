nums1 = [3, 2, 3, 1]
nums2 = [1, 2, 1, 3, 5, 6, 4]
nums3 = [1, 2, 1, 4, 5, 6, 4, 7]

nums = [nums1,
        nums2,
        nums3]

def Find_the_peak(array):
    n = len(array)
    peak_element = []
    
    if n == 1:
        return [0]

    if array[0] > array[1]:
        peak_element.append(0)

    for i in range(1, n - 1):
        if array[i - 1] <= array[i] >= array[i + 1]:
            peak_element.append(i)

    if array[n - 1] > array[n - 2]:
        peak_element.append(n - 1)

    return peak_element

for array in nums:
    peak_elements = Find_the_peak(array)
    print(f"Peak element index of : {array} -> {peak_elements}")
