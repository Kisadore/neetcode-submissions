class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap1 = Counter(s)
        hashMap2 = Counter(t)
        # hashMap1 = defaultdict(int)
        # hashMap2 = defaultdict(int)

        # for i in range(len(s)):
        #     hashMap1[s[i]] += 1
        #     hashMap2[t[i]] += 1

        if hashMap1 == hashMap2:
            return True
        else:
            return False
