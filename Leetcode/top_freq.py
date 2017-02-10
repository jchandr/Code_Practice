def mergesort(alist,mode):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergesort(lefthalf,mode)
        mergesort(righthalf,mode)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


def sortbycounts(rnk,numbers,k):
    t_rnk = rnk
    max = 0
    max_index = 0
    listofmax = []

    for i in range(0,len(t_rnk)):
        if(t_rnk[i] >= max):
            max = t_rnk   

    for temp in range(0,k):
        for i in range(0,len(t_rnk)):
            if ((t_rnk[i] <= max) and (not(i in listofmax))):
                max = t_rnk[i]
                max_index = i
                print(t_rnk)
        t_rnk[max_index] = 0
        listofmax.append(max_index)

    return listofmax
    
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    top = 0
    top_frequent = []
    rank_count = 0
    ranks = []
    mergesort(nums,0)
    print(nums)
    for i in nums:
        if(top != i):
            top_frequent.append(i)
        top = i

    top = nums[0]
    for i in nums:
        if(top == i):
            rank_count = rank_count + 1
        else:
            if(rank_count == 0):
                rank_count = 1
            ranks.append(rank_count)
            rank_count = 0
        top = i
    
    ranks.append(rank_count)

    print("numbers ",top_frequent)
    print("number of occurances",ranks)
    temp = sortbycounts(ranks,top_frequent,k)
    top_frequent = top_frequent[:k]
    return (temp)

rank = [0,0]
nums = [1,5,1,6,6,5,6,1,6,5,6,5,1,5,2,6,5,4,6]
print(topKFrequent(nums, 2))