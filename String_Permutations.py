def generate_permutations(s, i, result):
        if i == len(s):
            result.append(''.join(s))
        else:
            for j in range(i, len(s)):
                s[i], s[j] = s[j], s[i]
                self.generate_permutations(s, i + 1, result)
                s[i], s[j] = s[j], s[i]

def permutation(S):
      ans = []
      self.generate_permutations(list(S), 0, ans)
      ans.sort()
      return ans
