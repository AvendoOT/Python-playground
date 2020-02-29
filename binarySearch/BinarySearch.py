def binarySearchIterative(array, x):
    left = 0;
    right = len(array) - 1
    i = 0
    while (left <= right):
        i += 1
        mid = (left + right) // 2
        if (array[mid] == x):
            print("We found " + str(x) + " in " + str(i) + " attempts")
            return
        elif (x < array[mid]):
            right = mid - 1
        elif (x > array[mid]):
            left = mid + 1
    print("We didn't find " + str(x))
    return

def binarySearchRecursive(array, x, left, right, n):
    if (left > right):
        print("We didn't find " + str(x))
        return
    mid = (left+right)//2
    if (x < array[mid]):
        return binarySearchRecursive(array, x, left, mid-1, n+1)
    elif (x > array[mid]):
        return binarySearchRecursive(array, x, mid +1, right, n+1)
    elif (x == array[mid]):
        print("We found " + str(x) + " in " + str(n) + " attempts")
        return

sizeArray = int(input("Enter the size of an array"))
array = []
for i in range (sizeArray):
    array.append(int(input("Enter number")))
x = int(input("Enter the searching number"))
array.sort()
binarySearchIterative(array, x)
binarySearchRecursive(array, x, 0, len(array)-1, 1)













