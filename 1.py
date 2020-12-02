k = 2020
nums = []
try:
    while True:
        q = int(input())
        nums.append(q)
except: EOFError

nums.sort()
N = len(nums)
for i in range(N):
    low = i + 1 # First index in array
    high = N-1  # last index in array

    while high > low:
        if nums[i] + nums[low] + nums[high] == k:
            print(nums[i] * nums[low] * nums[high])
            exit(0)
        elif nums[i] + nums[low] + nums[high] > k:
            high -= 1
        else:
            low += 1
