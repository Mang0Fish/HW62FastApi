word_list = ['java', 'jjava', 'vaj', 'aavj', 'j', 'vjaa', 'dan', 'and', 'ddan']



# This is the full solution, but I only manage to do it after the
# short solution below.
# I added it, so you can see my thought process

words2 = {}
for i in word_list:
    if ''.join(sorted(list(i))) in [''.join(sorted(list(_))) for _ in words2.keys()]:
        i = ''.join(sorted(list(i)))
        x = ''
        for j in words2.keys():
            if i == ''.join(sorted(list(j))):
                x = j
                break
        words2[x] += 1
    else:
        words2[i] = 1

print(words2)

#--------------------------------------------------------------------------------------------

# Solution 2, This is the shorter solution which doesn't consider
# the first words structure
words = {}
for i in word_list:
    if ''.join(sorted(list(i))) in words.keys():
        words[''.join(sorted(list(i)))] += 1
    else:
        words[''.join(sorted(list(i)))] = 1

print(words)







