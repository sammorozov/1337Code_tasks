def find_sub(s, k):
 
    Len = len(s)
     
    # initialize left and right pointer to 0
    lp, rp = 0, 0
                 
    ans = 0
 
    # an array to keep track of count of each alphabet
    hash_char = [0 for i in range(256)]    
    for rp in range(Len):
 
        hash_char[ord(s[rp])] += 1
 
        while(hash_char[ord(s[rp])] > k):
            hash_char[ord(s[lp])] -= 1 # decrement the count
            lp += 1         #increment left pointer
 
        ans += rp - lp + 1
 
    return ans
 
s = "gvgvvgv"
k = 2
print(find_sub(s, k))
 

 '''
 всем спасибо! это был полный пиздец
 Рейтинг
 4040 / 15304	sammorozov 	7	0:29:47	0:03:55 	0:24:47 1	
 
 '''