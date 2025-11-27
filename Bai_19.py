arr = [1, 4, 7, 10, 12]
N = 15
closest_pair = None
min_diff = float("inf")
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        tong = arr[i] + arr[j]
        diff = abs(tong - N)
        if diff < min_diff:
            min_diff = diff
            closest_pair = (arr[i], arr[j])
print("Cặp gần nhất:", closest_pair)
print("Tổng:", sum(closest_pair))
