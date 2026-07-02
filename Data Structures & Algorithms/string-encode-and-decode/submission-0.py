class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + "#" + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        list_strs = []
        i = 0

        while i < len(s):
            delimiter_position =  s.find('#', i)
            length = int(s[i:delimiter_position])
            i = delimiter_position + 1

            list_strs.append(s[i:i + length])
            i += length

        return list_strs