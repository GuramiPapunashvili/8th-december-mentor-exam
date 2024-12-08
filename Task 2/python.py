def uniqueWords(s):
    count = 0 #simply create a variable keeping count of unique words
    arr = s.split(' ') #split the string we recive, so we only work with words
    def removePunctuation(arr): #create a simple function removing every punctuatuons
        res = [] #an array to keep the final result
        punctuation = ['.',',','!',':',';'] #we keep every punctuation in an array, we will see why later
        for i in arr: #simply go over every element in the arr to see which one is a punctuation
            if i not in punctuation: #if an element is not a in array named punctuation that means it is not a punctuation
                res.append(i) #so we append it to our result
            else:
                continue #if it is a punctuation we dont append it and simply continue
        return ' '.join(res) #finally we return the joined array of out result
    arr = [i.lower() for i in arr] 
    removePunctuation(arr)
    alreadyChecked = []
    for i in arr:
        if i not in alreadyChecked and i != '':
            count += 1
            alreadyChecked.append(i)
    return count


print(uniqueWords("The quick brown fox jumps over the lazy dog"))
