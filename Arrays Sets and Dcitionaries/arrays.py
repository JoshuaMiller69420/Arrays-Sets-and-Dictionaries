from array import array

numbers = array("i" , [1,2,3,4,5])

numbers.append(6)
numbers[2] = 99
numbers[3] = "Mosh is so dreamy"
print(numbers)
print(numbers[2])

