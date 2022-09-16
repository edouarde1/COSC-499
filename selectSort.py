def sortNums (numList):
    n = len(numList)
    for i in range(0,n): 
        curr_val = numList[i]
        # Find the min and swap 
        for j in range(i+1,n):
            next_val = numList[j]
            # Swap if there next value is less then current
            if (next_val < curr_val):
                temp = numList[i]
                numList[i] = numList[j]
                numList[j] = temp
                curr_val = next_val
    return numList

       
def sortChars (alphaList):
    unicodeList = []
    sortedChars = []
   
   # Convert into unicodes 
    for char in alphaList:
        unicodeList.append(ord(char))

   # Sort Unicodes
    sortedUnicode = sortNums(unicodeList)
    
    # Convert unicodes back to chars
    for num in sortedUnicode:
        sortedChars.append(chr(num))
    
    return sortedChars





