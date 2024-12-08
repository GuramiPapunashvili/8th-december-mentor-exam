def Xbonacci(num1,num2):
    res = [] #create an array for res
    for i in range(num1): #we go through the range if the number given to us
        while len(res) != num2: #we check to make sure the length of the result isnt equal to our max length(given as an argument), this is for cases when for example num2 equals 1
            res.append(1) #we append 1 in range of num1 
    while len(res) != num2: #while the length of the result doesnt equal the length we want we keep appending
        forAppend = num1 - num1*2 #i turn my number into a minus so we can append the sum of last N numbers
        res.append(sum(res[forAppend:])) #here we just append the sum of last N numbers
    return res #we simply return the result here
print(Xbonacci(3,1))

        