def merge_sort(arr,l,r):
    if(l<r):
        mid=(l+r)/2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1,r)
        merge_data(arr,l,mid,r)


def merge_data(arr,l,mid,r):
    i=l
    j=mid+1
    k=l
    while(i<=mid and j<=r):
        if(arr[i]>arr[j]):
            b[k]=arr[j]
            j+=1
        else:
            b[k]=arr[i]
            i+=1
            k+=1

    if(i>mid):
        while(j<=r):
            b[k]=arr[j]
            j+=1
            k+=1
    else:
        while(i<=mid):
            b[k]=arr[i]
            i+=1
            k+=1
    

            
