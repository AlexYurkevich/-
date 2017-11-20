#1.1
def min (array):
    for i in range (len(array)):
        minimum = array [0]
        if minimum > array[i]:
            minimum = array [i]
    return minimum


#1.2
def middle (array):
    x = 0
    for i in range (len(array)):
       x = array [i] + x
    y = x/len(array)
    return y
array = [1, 2, 3, 4, 5]
print ("1.1:",min(array))
print ("1.2:",middle(array))