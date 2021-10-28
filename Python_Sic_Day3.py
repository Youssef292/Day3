def PerfectSquare(list,a, b):
    my_list = []
    for j in range (list):
        X = int(input())
        my_list.append(X)
    print(my_list)
    for i in my_list:
        if (i*(.5) == int(i*(.5))):
            if (i>a and i<b):
                print(i)


# take inputs
elements = int(input("Enter list elements:"))
start = int(input('Enter start number: '))
end = int(input('Enter end number: '))


# calling function
PerfectSquare(elements, start, end)
