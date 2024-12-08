def KthSmallest(arr,num):
    sortedArr = sorted(arr) #we simply sort our given array here
    return sortedArr[num-1] #since our array is already sorted we simply return the NUMth number that is given to us, we do -1 since array starts counting from 0

print(KthSmallest([7, 10, 4, 3, 20, 15],3))