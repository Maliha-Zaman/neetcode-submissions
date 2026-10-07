class MinStack:
    
    def __init__(self):
         self.Minstack=[]
         self.Getmin=[]
      
         

    def push(self, val: int) -> None:
          
          self.Minstack.append(val)
          if(self.Getmin):
               val= min(self.Getmin[-1],val)
          self.Getmin.append(val)
          
               
    def pop(self) -> None:
         self.Minstack.pop()
         self.Getmin.pop()

    def top(self) -> int:
        return self.Minstack[-1]

    def getMin(self) -> int:
        return self.Getmin[-1]
        
