def isStraightHand(N, groupSize, hand):
        d = {}
        
        for i in hand:
            d[i] = d.get(i,0) + 1
            
        hand.sort()
        
        for i in hand:
            if not d[i]:
                continue
            
            for j in range(groupSize):
                curr = i + j
                if d.get(curr, 0) == 0:
                    return False
                    
                d[curr] -= 1
        
        return True
