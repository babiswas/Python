def partition(arr,start,end):
   wall=start-1
   fix=arr[end-1]
   for i in range(start,end-1):
     if arr[i]<fix:
        wall=wall+1
        arr[wall],arr[i]=arr[i],arr[wall]
   wall=wall+1
   arr[wall],arr[end-1]=arr[end-1],arr[wall]
   return wall

def qsort(arr,start,end):
    if start<end:
       index=partition(arr,start,end)
       qsort(arr,start,index)
       qsort(arr,index+1,end)

if __name__=="__main__":
   arr=[12,1,2,21,0,5,4,3]
   qsort(arr,0,len(arr))
   print(arr)
   
   