const selectSortNums = function (array) {
    // 1. Keep track of current value i 
    // 2. Keep track of start of secdary array. i+1 
    // 3. Iterate through the secondary array and sawp elements if need be 

    for(i = 0; array.length()-1; i++) {
        //Current value intialized
        let v1 = list[i]
        
        // Find next min value 
        for(j=i+1; array.length()-1; j++) {
            
            let v2 = list[j]

            // Swap values if their is a min present
            if (v2 < v1) {
                let temp = list[i]
                list[i] = v2
                list[j] = temp
                
            }

        }
    }


    



    

}