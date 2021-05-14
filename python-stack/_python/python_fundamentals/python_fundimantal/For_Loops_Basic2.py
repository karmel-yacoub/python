# 1-Biggie Size 
def biggie_size (list):
    for i in range(0,len(list),1):
       if list[i]>0:
           list[i]="big"
    return list
print(biggie_size([-1, 3, 5, -5]))        

# 2-Count Positives
def count_positives(list):
    count=0
    for i in range(0,len(list),1):
        if list[i]>0:
            count+=1
    list[len(list)-1]=count
    return list
print(count_positives([1,6,-4,-2,-7,-2]))

# 3-Sum Total
def sum_total (list):
    sum=0
    for i in range(0,len(list),1):
        sum+=list[i]
    return sum
print(sum_total([1,2,3,4]))

# 4-Average
def average(list):
    sum=0
    for i in range(0,len(list),1):
        sum+=list[i]
    average=sum/len(list)
    return average
print(average([1,2,3,4]))
       
# 5-Length
def length (list):
    for i in range(0,len(list),1):
        return len(list)
print(length([37,2,1,-9]))

# 6-Minimum
def minimum(list):
    for i in range(0,len(list),1):
        x=min(list)
        return x
    if len(list)==0:
        return "false"
print(minimum([37,2,1,-9]))

# 7-Maximum 
def maximum(list):
    for i in range(0,len(list),1):
        x=max(list)
        return x
    if len(list)==0:
        return "false"
print(maximum([37,2,1,-9]))

# 8-Ultimate Analysis 
def ultimate_analysis(list):
    sum_total = sum(list)
    average = sum(list)/len(list)
    minimum = min(list)
    maximum = max(list)
    length = len(list)
    analysis={
            'sum_total':sum_total,
            'average':average,
            'maximum':maximum,
            'length':length,
            'minimum':minimum
    }
    return analysis
print(ultimate_analysis([37,2,1,-9]))

# 9-Reverse List
def reverse_list(list):
    for i in range(0,len(list),1):
        return list[::-1]
print(reverse_list([37,2,1,-9]))
