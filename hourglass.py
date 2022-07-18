def hour_glass_sum(arr):
    b=[0]*16
    k=0
    for i in range(6):
        for j in range(6):
            try:
                upa=arr[i][j]
                upb=arr[i][j+1]
                upc=arr[i][j+2]
                mid=arr[i+1][j+1]
                bota=arr[i+2][j]
                botb=arr[i+2][j+1]
                botc=arr[i+2][j+2]
                b[k]=upa+upb+upc+mid+bota+botb+botc
                k+=1
            except:
                continue
    return max(b)

