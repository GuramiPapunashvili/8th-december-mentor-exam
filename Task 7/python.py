def primeInRange(num1,num2):
    res = [] #create an array where i keep result
    def checkPrime(num): #we create a function for checking a prime
        for i in range(2,num): #iterate through every number between 2 and our number
            if num2 % i == 0: #since we're not taking 1 and the number itself into account it shouldnt have any divisors, so if it does we instantly return False
                return False 
        return True #if it doesnt have any divisors we return true
    for i in range(num1,num2): #now we go through the range given
        if i == 1: #since 1 is not considered a prime but will pass the requirments we single it out using if
            continue
        elif checkPrime(i): #otherwise if a number is a prime we append it to the result
            res.append(i)
    return res

print(primeInRange(24,25))
print(primeInRange(10,20))
print(primeInRange(1,10))
print(primeInRange(20,30))
print(primeInRange(1,1))
