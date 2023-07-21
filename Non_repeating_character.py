def nonrepeatingCharacter(self,s):
      d={}
      for i in s:
          if(i in d):
              d[i]+=1
          else:
              d[i]=1
              
      for i in s:
          if(d[i]==1):
              return i
              break
          
      return "$"
