# # Bucket sort algorithm 

# nums = [1,1,1,2,2,3] # best solution is to use the length on the input to create buckets
# # each sub arr represent the num of times that the number occured  
# k = 2
# # Output: [1,2]

# def topKFrequent(nums, k):
#     count = {}
#     freq = [[] for n in range(len(nums) + 1)]  # [ [],[],[],[],[],[] ]

#     for n in nums:
#         count[n] = 1 + count.get(n, 0) # get garantee default 0
    
#     # print(count.items())
#     for n, c in count.items(): # gives [(k,v)] list of tuples from the dictionary 
#         freq[c].append(n) # c is number of ocurrences and n is the actual number

#     f = len(freq) - 1
#     res = []
#     while len(res) < k:
#         if not freq[f]:
#             f -= 1
#         else:
#            last = freq[f].pop()
#            res.append(last)


#     # count = {}
#     # freq = [[] for i in range(len(nums) + 1)]

#     # for n in nums:
#     #     count[n] = 1 + count.get(n, 0)
#     # for n, c in count.items():
#     #     freq[c].append(n)

#     # res = []
#     # for i in range(len(freq) - 1, 0, -1):
#     #     for n in freq[i]:
#     #         res.append(n)
#     #         if len(res) == k:
#     #             return res

#     return res 

# print(topKFrequent(nums, k))


def topKFrequent(self, nums, k: int):
     # store in a hashmap number of ocurances
    count = {}

    # list of sub list that goes from zero to len(list) + 1
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # iterate hashmap val are going to be the index of the list above, append the key at the index bucket
    for c, v in count.items():
        freq[v].append(c)

    # set res variable to list
    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            # for each sublist pop last element and push to res
            res.append(n)
            if len(res) == k:
                return res
    # # if lenght of res = to k return res
