class Search:
    def __init__(self,arr,value):
        self.arr=arr
        self.value=value
    def binary_search(self):
        lower=0
        upper=len(self.arr)-1
        self.arr.sort()
        while(lower<upper):
            mid=(lower+upper)//2
            if(self.arr[mid]==self.value):
                print("Found Value At:  "+str(mid))
                print("Given Arr: "+str(self.arr))
                print("Given Value: "+str(self.value))
                return True
            elif(self.arr[mid]>self.value):
                upper=mid
                print("changing Upper")
            else:
                lower=mid
                print("changing Lower")

