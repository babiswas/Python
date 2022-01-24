def bubble_sort(arr):
   for i in range(len(arr)):
     for j in range(len(arr)-i-1):
         if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__=="__main__":
   arr=[22,10,4,6,1,15,12,9,16]
   bubble_sort(arr)
   print(arr)