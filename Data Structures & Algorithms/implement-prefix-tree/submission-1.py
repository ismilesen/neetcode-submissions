class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

        #hashmap of children allows for character and branch to be saved

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        #when the tree is none you can simply insert every node of the word and have the last node given self.end

    def search(self, word: str) -> bool:
        
        #dfs search i think. maybe we chose left or right based on prefixes
        #insert into stack the word characters.
        #chech stack together with what we found in the prefix.
        #check word end mark
        #return True if not base case of return false
        #overengineering
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        #finding subwords of prefixes
        