class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #base case solution for 2 digit 
        if not digits:
            return []
        res = []
        digsToChar = {  "2" : "abc",
                        "3" : "def",
                        "4" : "ghi",
                        "5" : "jkl",
                        "6" : "mno",
                        "7" : "pqrs",
                        "8" : "tuv",
                        "9" : "wxyz"
                        }
        print(digits)

        def backTracker(i, currString):

            if len(currString) == len(digits):
                res.append(currString)
                return
            for c in digsToChar[digits[i]]:
                backTracker(i + 1, currString + c)

        backTracker(0, "")
        return res