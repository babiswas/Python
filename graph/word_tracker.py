import copy
def issafe(x,y,length,breadth,M,new_target):
    if x<0 or x>=length:
       return False
    if y<0 or y>=breadth:
       return False
    if M[x][y]!=new_target:
       return False
    return True

def find_word(M,str1,target,x,y,path,visited,length,breadth,target_list,l):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    visited[x][y]=True
    path.append((x,y))
    str1+=M[x][y]
    if str1==target:
       l[0]=True
       return
    else:
       new_target=target_list.pop(0)
       for i in range(4):
           X=x+dx[i]
           Y=y+dy[i]
           if issafe(X,Y,length,breadth,M,new_target):
              if visited[X][Y]==False:
                 find_word(M,str1,target,X,Y,path,visited,length,breadth,target_list,l)
       if l[0]==False:
         path.pop()
         str1=str1[:-1]
      
def word_tracker(word):
   M=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
   visited=[[False for i in range(4)] for i in range(3)]
   path=list()
   target_list=list(word)
   target_list.pop(0)
   str1=''
   l=list()
   l.append(False)
   find_word(M,str1,word,0,0,path,visited,3,4,target_list,l)
   str2=''
   for u,v in path:
      str2+=M[u][v]
   print(str2)


if __name__=="__main__":
  word_tracker("ABCCED")
  