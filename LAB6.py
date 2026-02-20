# Merge Sort Algo
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    sorted_result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_result.append(left[i])
            i += 1
        else:
            sorted_result.append(right[j])
            j += 1

    sorted_result.extend(left[i:])
    sorted_result.extend(right[j:])
    
    return sorted_result

if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original array: {sample_array}")
    
    sorted_array = merge_sort(sample_array)
    print(f"Sorted array:   {sorted_array}")