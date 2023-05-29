def check(word, Pattern):
    i = 0
    j = 0
    
    while i < len(word) and j < len(Pattern):
        if word[i] == Pattern[j]:
            if j == len(Pattern)-1:
                return word
            i += 1
            j += 1
        
        elif word[i].isupper() and word[i] != Pattern[j]:
            return -1
                
        else:
            i += 1
    
    return -1
  
  def CamelCase(self,N,Dictionary,Pattern):
    res = []
        
    for word in Dictionary:
        following = check(word, Pattern)
        if following != -1:
            res.append(following)
                
    if len(res) == 0:
        return [-1]
    return res
