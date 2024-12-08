def validateSudoku(arr):
    forColumn = [] #i create an array which i will later use to store the columns of our table
    nums = '123456789' #i keep numbers 1-10 in this string so later if a number is not in the list(for example if it is 10 or even 0)
    for i in arr: #i iterate through the array
        for x in i: #since the we have a 2D table it will return another table which im gonna iterate through once again
            if i.count(x) > 1: #if our number appears in a row more than once we instantly return False
                return False
            if str(x) not in nums: #or if our number is not in nums meaning its either 0 or more than 9, we return False
                return False
    for i in range(9): #now to calculate columns, we write a range of 9 because we have to calculate 9 rows
        forColumn = [] #we clear the column before each loop so we dont get multiple rows mixed up
        for i in range(9): #once again write a range of 9 so because theres 9 elements in each column
            for x in arr: #now iterate through the arr and take the first element of each array on line 15
                if len(forColumn) < 9: #if the length of our column arr is not 9 yet we append the number if it is it will simply continue
                    forColumn.append(x[0])
        for i in forColumn: #now iterate through the column and make simple checks
            if forColumn.count(i) > 1: #if a numbers appears more than once immediate False
                return False
            if str(i) not in nums: #if a number is not in nums it means its either a 0(or a negative number) or more than 9, in both cases instant False
                return False
    return True #if our array gets through all the checks its valid so we return True

print(validateSudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 9, 7, 9]]))




        