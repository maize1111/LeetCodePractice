class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word is None:
            return False
        return self.find(self.root, word, 0)

    def find(self, node, word, index):
        if node is None:
            return False
        if index >= len(word):
            return node.isWord
        char = word[index]
        if char != '.':
            return self.find(node.children.get(char), word, index)

        for child in node.childs:
            if self.find(node.children[child], word, index + 1):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
obj = WordDictionary()
obj.addWord("fuck")
obj.addWord("you")
print(obj.search("you"))
