def pick_peaks(arr):
    if not arr:
        return {"pos":[],"peaks":[]}
        
    diff_arr = []
    for i in range(len(arr) - 1):
        diff_arr.append(arr[i+1] - arr[i])
    possible_peak = 0
    position_arr = []
    for i in range(len(diff_arr)):
        if diff_arr[i] > 0:
            possible_peak = i + 1
        elif diff_arr[i] < 0:
            if possible_peak:
                position_arr.append(possible_peak)
            possible_peak = 0
    peaks_arr = []
    for i in position_arr:
        peaks_arr.append(arr[i])
    return {"pos": position_arr, "peaks": peaks_arr}