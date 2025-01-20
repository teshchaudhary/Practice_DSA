# Given a number N. Find the length of the longest consecutive 1s in its binary representation.
# by doing the and of the number with it's right shifted bits or right shifted bits we keep decreasing the 1s in the pattern.
# In 1st iteration: 
#                             N=222        :          1 1 0 1 1 1 1 0
#                             (N<<1)       :          1 0 1 1 1 1 0 0
#                   N = (N & (N << 1))     :          1 0 0 1 1 1 0 0 
# In 2nd iteration: 
#                             N            :          1 0 0 1 1 1 0 0
#                            (N<<1)        :          0 0 1 1 1 0 0 0
#                  N = (N & (N << 1))      :          0 0 0 1 1 0 0 0 
# In 3nd iteration: 
#                             N            :          0 0 0 1 1 0 0 0
#                            (N<<1)        :          0 0 1 1 0 0 0 0
#                  N = (N & (N << 1))      :          0 0 0 1 0 0 0 0 
# In 4th iteration: 
#                             N            :          0 0 0 1 0 0 0 0
#                            (N<<1)        :          0 0 1 0 0 0 0 0
#                  N = (N & (N << 1))      :          0 0 0 0 0 0 0 0 

def maxConsecutiveOnes(N):
    res = 0
    
    while N:
        res += 1
        N = N&(N>>1)
        # N = N&(N>>1) This can also be used
    return res
