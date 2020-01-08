n=int(input("Number of Elements: "))
elements=input("Enter Array Elements \'separated by space\':\n")
array=elements.split(" ")
if n is not len(array):
    print("Given \'array count\' or \'format\' doesn't match. Provide Valid data")
else:
    sum=0
    for i in array:
        sum+=int(i)
    avg=int(sum/n)
    print(avg+1)