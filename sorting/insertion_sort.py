def insertion_sort(arr):
   for i in range(1,len(arr)):
      fix=arr[i]
      hole=i
      if hole-1>=0:
         while arr[hole-1]>fix and hole-1>=0:
             arr[hole]=arr[hole-1]
             hole=hole-1
      arr[hole]=fix
if __name__=="__main__":
   arr=[12,1,3,4,21,6,7,1]
   insertion_sort(arr)
   print(arr)
             