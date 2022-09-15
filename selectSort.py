
    # 1. Keep track of current value i 
    # 2. Keep track of start of secondary index. i+1 
    # 3. Iterate through the secondary array and swap current with min if need be 


def sortNums (list):
    n = len(list)
    for i in range(0,n): 
        curr_val = list[i]
        # Find the min and swap 
        for j in range(i+1,n):
            next_val = list[j]
            # Swap if there next value is less then current
            if (next_val < curr_val):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                curr_val = next_val



              
    
    return list


print(sortNums([5,2,3,4,1]))

