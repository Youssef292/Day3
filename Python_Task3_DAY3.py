def PerfectSquare(a, b):
    for i in range(a, b + 1): 
        if (i**(.5) == int(i**(.5))): 
            print(i, end=" ") 

# take inputs
start = int(input('Enter start number: '))
end = int(input('Enter end number: '))
print('All perfect square')

# calling function
PerfectSquare(start, end)