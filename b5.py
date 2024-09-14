def mysum(my_list):
    result = 0
    for i in range(0,len(my_list)):
        result = result + my_list[i]
    return result


list1 = [8,3,0,2,7]

print(mysum(list1))
