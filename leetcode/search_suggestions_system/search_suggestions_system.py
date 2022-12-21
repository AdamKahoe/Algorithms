class TrieNode(object):
    def __init__(self):
        self.words = []
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)
            node.words.sort()
            if len(node.words) > 3:
                node.words = node.words[:3]

    def search(self, word):
        result, node = [], self.root
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            result.append(node.words[:])
        for _ in range(len(word) - len(result)):
            result.append([])
        return result

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        trie = Trie()
        for product in products:
            trie.insert(product)
        return trie.search(searchWord)