def longestPalinSubseq(self, S):
      l = len(S)
      rev = S[::-1]
      
      dp = [[0 for i in range(len(S)+1)] for j in range(len(S)+1)]
      
      for i in range(1,l+1):
          for j in range(1,l+1):
              if(S[i-1] == rev[j-1]):
                  dp[i][j] = 1 + dp[i-1][j-1]
              else:
                  dp[i][j] = max(dp[i-1][j],dp[i][j-1])
      ans=  0
      for i in dp:
          for j in i:
              res = max(ans,j)
      return res
