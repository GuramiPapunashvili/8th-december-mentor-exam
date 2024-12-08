def pascalTriangle(num):
    rows = []  # Create an array to keep the result
    for i in range(num):  # Iterate through each number in num
        row = [1] * (i + 1)  # Create a row with (i + 1) elements, all 1's
        for x in range(1, i):  #change the elements between the first and last element
            row[x] = rows[i - 1][x - 1] + rows[i - 1][x]  # Add values from the previous row
        rows.append(row)  # Append the row to the rows list
        print(row)  # Print the row

pascalTriangle(5)
pascalTriangle(1)
pascalTriangle(2)
pascalTriangle(3)
pascalTriangle(0)

    

        
