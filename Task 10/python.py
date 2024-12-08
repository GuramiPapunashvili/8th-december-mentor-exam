def tooLazyToComeUpWithGoodName(t1,t2):
    def calculateLCM(num1,num2):
        for i in range(1,num1*num2):
            if num1 % i == 0 and num2 % i == 0:
                return i
    def calculateGCD(num1,num2):
        return num2 == 0 and num1 or calculateGCD(num2, num1 % num2)
    LCMOfdenominators = calculateLCM(t1[1],t2[1])
    GCDOfdenominators = calculateGCD(t1[1],t2[1])
    return (t2[0] * t2[1]) / LCMOfdenominators + (t1[0] * t1[1]) / LCMOfdenominators

print(tooLazyToComeUpWithGoodName((1,2),(1,3))) #not working btw


