def CaesarCipher(s,num):
    res = [] #create an array where we keep out result
    punctuation = ['.',',','!',':',';'] #create a array with punctuations so we dont accidently change them and replace them, when were not supposed to
    arr = [i for i in s] #simply keep all the elements of our string in an array
    alphabet = 'abcdefghijklmnopqrstuvwxyz' #string of every letter so we can use indexing later to replace needed elements
    for i in arr: #loop through the array so we can change whats neccesary
        if i in punctuation or i == ' ': #if our element is a space or a punctuation we append it without changing it
            res.append(i)
        else:
            if alphabet.index(i.lower()) + num > 26: #we check if the elements index + the number we have to affect it by is more than the length of our string
                res.append(alphabet[26 - alphabet.index(i.lower()) + num - 1]) #if it is we simply calculate how much it is more by, so if it is more by N we take the Nth number in the alphabet from the start
            else:
                res.append(alphabet[alphabet.index(i.lower()) + num]) #if it isnt we simply append the letter that is five spaces after our current number
    return ''.join(res) #finally we just return the joined version of our result


print(CaesarCipher("abc", 2))
print(CaesarCipher("xyz", 3))
print(CaesarCipher("Python", 0))
print(CaesarCipher("abc", -1))
print(CaesarCipher("Hello, World!", 5))
