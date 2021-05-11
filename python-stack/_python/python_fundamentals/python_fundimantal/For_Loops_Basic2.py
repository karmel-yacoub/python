# 1-Biggie Size 
# def biggie_size (list):
#     for i in range(0,len(list),1):
#        if list[i]>0:
#            list[i]="big"
#     return list
# print(biggie_size([-1, 3, 5, -5]))        

# 2-Count Positives
# def count_positives(list):
#     count=0
#     for i in range(0,len(list),1):
#         if list[i]>0:
#             count+=1
#     list[len(list)-1]=count
#     return list
# print(count_positives([1,6,-4,-2,-7,-2]))

# 3-Sum Total
# def sum_total (list):
#     sum=0
#     for i in range(0,len(list),1):
#         sum+=list[i]
#     return sum
# print(sum_total([1,2,3,4]))

# 4-Average
# def average(list):
#     sum=0
#     for i in range(0,len(list),1):
#         sum+=list[i]
#     average=sum/len(list)
#     return average
# print(average([1,2,3,4]))
       
# 5-Length
# def length (list):
#     for i in range(0,len(list),1):
#         return len(list)
# print(length([37,2,1,-9]))

# 6-Minimum
# def minimum(list):
#     for i in range(0,len(list),1):
#         x=min(list)
#         return x
#     if len(list)==0:
#         return "false"
# print(minimum([37,2,1,-9]))

# 7-Maximum 
# def maximum(list):
#     for i in range(0,len(list),1):
#         x=max(list)
#         return x
#     if len(list)==0:
#         return "false"
# print(maximum([37,2,1,-9]))

# 8-Ultimate Analysis 
def ultimate_analysis(list):
    sumtotal=0
    for i in range(0,len(list),1):
        

        sumtotal+=list[i]
        x=min(list)
        y=max(list)
    avg=sumtotal/len(list)
    return dict
    print(ultimate_analysis([37,2,1,-9]))

 


