def selection_sort(arr):
   for i in range(len(arr)):
     if i+1<len(arr):
       for j in range(i+1,len(arr)):
          if arr[i]>arr[j]:
             arr[i],arr[j]=arr[j],arr[i]

if __name__=="__main__":
   arr=[12,10,1,4,2,20,6,3,11]
   selection_sort(arr)
   print(arr)
   arr=[-1,-5]
   selection_sort(arr)
   print(arr)
          