

array = [2,4,6,8,9,7,5,3,1,10]

def find_max_recursive(array,n):
    if n == 1: 
        return array[0]
    else: 
        return array[0] if array[0] > find_max_recursive(array[1:],n-1) else find_max_recursive(array[1:], n-1)


def find_max_iterative(array,n):
    maxValue = array[0]
    for i in range(1,len(array)):
        if array[i] > maxValue:
            maxValue = array[i]

    return maxValue


recMaxValue = find_max_recursive(array,len(array))
print("재귀 최대 함수 값:", recMaxValue)

iterMaxValue = find_max_iterative(array,len(array))
print("반복 최대 함수 값:", iterMaxValue)


