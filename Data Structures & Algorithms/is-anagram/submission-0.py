class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        for char in s:
            if char not in hashMap1:
                hashMap1[char] = 1
            else:
                value_count = hashMap1.get(char)
                hashMap1[char] = value_count + 1

        for char in t:
            if char not in hashMap2:
                hashMap2[char] = 1
            else:
                value_count = hashMap2.get(char)
                hashMap2[char] = value_count + 1

        hashMap1_keys = sorted(list(hashMap1.keys()))
        hashMap2_keys = sorted(list(hashMap2.keys()))

        hashMap1 = {i : hashMap1[i] for i in hashMap1_keys}
        hashMap2 = {i : hashMap2[i] for i in hashMap2_keys}

        if hashMap1 == hashMap2:
            return True
        else:
            return False