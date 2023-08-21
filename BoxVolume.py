class BoxVolume():
  def computeB1B2Volume(self,l1:int, w:int, h:int )->int:
   if l1<=0 or w<=0 or h<=0:
    return 0 
   else:
     return 2*l1*w*h+l1*w*h
   
b1b2=BoxVolume()
print(b1b2.computeB1B2Volume(3,4,4))
