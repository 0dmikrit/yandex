def merge(left_half, right_half):
    merged_arr = []
    i, j = 0, 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            j += 1
    merged_arr += left_half[i:]
    merged_arr += right_half[j:]
    return tuple(merged_arr)