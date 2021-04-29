numList = []
number = int(input("please input the total number of elements in the list:"))
for i in range (1 , number + 1):
    value = int(input("please enter value of %d element:" %i))
    # inserts elements in the list
    numList.append(value)

print("\n positive number in the list are :")
# checks the entered number whether  it is positive or negative 
for j in range (number):
    if (numList[j]>=0):
        # prints the positive numbers
        print(numList[j], end=' , ')