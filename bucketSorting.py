import math
A =[11,4,21,8,17,13,14,1,24,12,21,22]
print("unsorted list: ",A)
maxmimum = max(A)
minimum = min(A)
Range = maxmimum-minimum
bucket=[]
n=5
for i in range(len(A)):
     bucket.append([]) #generated blank list into list of A[].
     
for j in A:
    index=math.ceil(j/n)
    bucket[index].append(j)
    
for i in range(len(A)):
    bucket[i] = sorted(bucket[i])
    
 
p=0
for i in range (len(A)):
    for j in range(len(bucket[i])):
        A[p]=bucket[i][j]
        p=p+1
print("sorted list: ",A)       
 