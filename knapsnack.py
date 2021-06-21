def knap_sack(capacity,weight,profit,item):
    if(item == 0 or capacity == 0):
        return 0
    if(weight[item-1]>capacity):
        return knap_sack(capacity,weight,profit,item-1)
    else:
        return max(profit[item-1]+knap_sack(capacity-weight[item-1],weight,profit,item-1),knap_sack(capacity,weight,profit,item-1))
print("Enter the profit : ")
profit = list(map(int,input().split(" ")))
print("Enter the weights : ")
weight = list(map(int , input().split(' ')))

while(True):
    capacity = int(input("Your max capacity : "))
    if(capacity == 0):
        print( 0)
        break
    item = len(weight)
    print(knap_sack(capacity,weight,profit,item))