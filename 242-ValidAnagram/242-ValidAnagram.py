# Last updated: 16/07/2025, 21:23:49
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = len(s)
        b = len(t)

        if a == b:
            hashmap1 = dict()
            hashmap2 = dict()
            
            for i in range(a):
                if s[i] in hashmap1:
                    hashmap1[s[i]] += 1
                else:
                    hashmap1[s[i]] = 1

                if t[i] in hashmap2:
                    hashmap2[t[i]] += 1
                else:
                    hashmap2[t[i]] = 1

            for i in hashmap1:
                if i not in hashmap2 or hashmap1[i] != hashmap2[i]:
                    return False

            return True
        else:
            return False
