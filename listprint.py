
my_list=[1,2,3,4,5,6,7]

def listele(i,arr):
    if(i>=len(arr)):
        return
    print(arr[i])
    listele(i+1,arr)
    
listele(0,my_list)
    