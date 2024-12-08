def checkAnagram(s1,s2):
    arr = [i for i in s2] #created an array where i keep every symbol in s2
    for i in s1: #used a for loop so iteration variable "i" gets the value of every element in s1
        if i not in arr: #i will eventually equal every element in s1, so if s1 is not in arr(where we keep every element in s2), we return False
            return False
        else:
            arr.remove(i) #if it IS in s2, we remove the said element
    if len(arr) != 0: #if the length of the array equals 0, it means that every single element got removed threfore every single element equaled the elements in s1, if s1 was longer than s2 it would return false because we use the for loop on s1
        return False
    return True

print(checkAnagram('silent','listen'))
