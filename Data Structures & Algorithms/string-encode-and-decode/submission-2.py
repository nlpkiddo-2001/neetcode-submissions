class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        # 4#neet
        result = []
        i = 0
       
        while i < len(s):
            j = i

            while s[j]!="#":
                j += 1

            length = int(s[i:j])
            j += 1

            string = s[j : j + length]
            result.append(string)

            i = j + length
        
        return result
    