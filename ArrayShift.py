class ArrayShift(object):
 def toWhichDirection(self,abdullah_array:list,mohammed_array:list)->str:
     sss=int(len(abdullah_array)/2)
     if len(abdullah_array) %2==1:
         sss+=1

     for i in range(1,sss):
         lis=abdullah_array[i:]+abdullah_array[:i]
         if lis==mohammed_array:
             return 'L'
     return 'R'    
 print(o.toWhichDirection([1,2,3],[1,2,3]))#R
print(o.toWhichDirection([1,2,3],[2,3,1]))#L
print(o.toWhichDirection([1,2,3],[3,1,2]))#R
print(o.toWhichDirection([1,2,3,4,5],[4,5,1,2,3]))#R
print(o.toWhichDirection([1 ,2 ,3,4,5],[5,1,2,3,4]))#R

print(o.toWhichDirection([1,2,3,4],[1,2,3,4]))#R
print(o.toWhichDirection([1,2,3,4],[2,3,4,1]))#L
print(o.toWhichDirection([1,2,3,4],[3,4,1,2]))#R
print(o.toWhichDirection([1,2,3,4],[4,1,2,3]))#R