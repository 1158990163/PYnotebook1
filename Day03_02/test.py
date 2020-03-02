
"""with open('C:\\Users\\1\\Desktop\\alice.txt', 'r', encoding='utf-8')as f:
    line = f.read().lower()
    for i in r',.?,)\'\"(`!:-*_;\\':
        line = line.replace(i, ' ')
    words_noSet=list(line.split())
    words_Set = list(set(line.split()))
    wordlist = []
    temp=0;
    for i in words_Set:
        for j in words_noSet:
            if i==j:
                temp+=1
        wordlist.append((i,temp))
        temp=0
"""
nums=[1,2,4,3,1,2,2132,5324,35,23,213,53,2314]
nums=list(set(nums))
nums.sort()
#list(set(nums)).sort()
print(nums)




    #for i in words:
    #    wordlist.append((i, len(re.findall(i, line))))
    #    print(wordlist)
