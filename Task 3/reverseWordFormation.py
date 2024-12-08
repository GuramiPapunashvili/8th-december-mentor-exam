def reverseWordFormation(s):
    arr = s.split(' ') #we simply split the string here so we only work with words
    if s == '': #if out string equals '' we simply return ''
        return ''
    return ' '.join(arr[::-1]) #otherwise we just return reversed version of our array, because of slicing our array is read from right to left instead of left to right
print(reverseWordFormation(''))