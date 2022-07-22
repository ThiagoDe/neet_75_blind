def groupAnagrams(strs):
    res = {}
    for s in strs:
        # print(s)
        sortedS = ''.join(sorted(s))
        # print(sortedS)
        if sortedS not in res:
            res[sortedS] = [s]
        else:
            res[sortedS].append(s)

    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))