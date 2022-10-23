import collections
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True
    
    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.childre:
                return False
            node = node.children[char]
        return True

trie = Trie()
word_list = list()
floor_provisions_info_cnt = int(input())
for _ in range(floor_provisions_info_cnt):
    provisions_info_list = input().split()
    for provisions_info in provisions_info_list[1:]:
        trie.insert(provisions_info)
        word_list.append(provisions_info)

for word in word_list:
    print(f"{trie.search(word)=}")