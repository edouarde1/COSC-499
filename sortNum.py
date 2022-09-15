
    # 1. Keep track of current value i 
    # 2. Keep track of start of secondary index. i+1 
    # 3. Iterate through the secondary array and sawp current with min if need be 


def sortNums (list):
    n = len(list)
    for i in range(0,n): 
        v1 = list[i]
        for j in range(i+1,n):
            v2 = list[j]
            # Swap if there v1 is there is a smaller val 
            if (v2 < v1):
                temp = list[i]
                list[i] = v2 
                list[j] = temp 
    return list


    

