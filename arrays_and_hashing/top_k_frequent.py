# Bucket sort algorithm 

nums = [1,1,1,2,2,3]
k = 2
# Output: [1,2]

def topKFrequent(nums, k):
    count = {}
    freq = [[] for n in range(len(nums) + 1)]  # [ [],[],[],[],[],[] ]

    for n in nums:
        count[n] = 1 + count.get(n, 0) # get garantee default 0
    
    for n, c in count.items():
        freq[c].append(n)

    f = len(freq) - 1
    res = []
    while len(res) < k:
        if not freq[f]:
            f -= 1
        else:
           last = freq[f].pop()
           res.append(last)

    return res 

print(topKFrequent(nums, k))