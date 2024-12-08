def Primorial(num):
    res = 1 #we make the res 1 since if it was 0, multiplying simply wouldnt work
    def checkPrime(num2): #we make a function to check if a number is prime
        for i in range(2,num2): #iterate through every number between 2 and our number
            if num2 % i == 0: #since we're not taking 1 and the number itself into account it shouldnt have any divisors, so if it does we instantly return False
                return False
        return True #if it doesnt have any divisors we return true
    for i in range(2,num+1): #now we go through the range from 2 to our number, +1 since we want to INCLUDE our number
        if checkPrime(i): #if the number is prime we multiply it to the result
            res *= i
    return res #and we return the result
print(Primorial(11))