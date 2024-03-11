def search_two_min(arr):
            
    min1 = min(arr)

    arr.remove(min1)

    min2 = min(arr)

    return min1, min2


print(search_two_min([1, 2, 10 ,3, -1, 2, 0]))


'''
https://www.youtube.com/watch?v=msztlG4FF3o&list=PLP446CXRka0WSd_go9mNmlFTXnFewh0S_&index=1

'''