# 1- Countdown
def countDown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList
print(countDown(5))

# 2-Print and Return 
def print_and_return(list):
    print(list[0])
    return list[1]   
print(print_and_return([3,5]))

# 3-First Plus Length 
def first_plus_length(list):
    return(list[0]+len(list))
print(first_plus_length([1,2,3,4,5]))

# 4-Values Greater than Second 
def values_greater_than_second(list):
    newlist=[]
    for i in range(0,len(list),1):
        if list[i]>list[1]:
            newlist.append(list[i])
    return(newlist)
print(values_greater_than_second([5,2,3,2,1,4])) 

# 5-This Length,That Value
def  length_and_value(size,value):
    list=[]
    for i in range(0,size,1):
        list.append(value)
    return list
print(length_and_value(4,7))    

