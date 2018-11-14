def wordBreak(s, wordDict):
    ranges = {}
    for word in wordDict:
        ranges[word] = []
    for word in wordDict:
        temp = s
        templen = 0
        while word in temp:
            start = s.index(word)
            end = start + len(word)
            ranges[word].append([start + templen, end + templen])
            templen += len(word)
            temp = temp[0:start] + temp[end:]
            print(temp)
    print(ranges)

wordBreak('applepenapple', ['apple', 'pen'])