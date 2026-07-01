class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        n = len(s)
        i = 0
        j = n - 1
        while i < n and j > 0:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True