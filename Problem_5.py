from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False

    def insert(self, char):
        self.children[char] = TrieNode(char)

    def suffixes(self, suffix=''):
        if self.children:
            for char, node in self.children.items():
                if node.is_end_of_word:
                    a.append(suffix + char)
                node.suffixes(suffix + char)
        return a


class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def insert(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.insert(letter)
            curr_node = curr_node.children[letter]
        curr_node.is_end_of_word = True

    def find(self, prefix):
        cur = self.root
        try:
            for letter in prefix:
                cur = cur.children[letter]
            return cur
        except:
            print("prefix does not exist")

MyTrie = Trie()
a = []
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
curr = MyTrie.root

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f, prefix='an')
"""
it should return t
thology
tagonist
tonym
"""


MyTrie = Trie()
a = []
wordlist2=["hey","hell","hello","water","waterfall","watercheastnut"]
for word in wordlist2:
    MyTrie.insert(word)
curr = MyTrie.root

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f, prefix='water')
"""
it should return
fall
cheastnut
"""


MyTrie = Trie()
a = []
wordlist3=[]
for word in wordlist3:
    MyTrie.insert(word)
curr = MyTrie.root

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f, prefix='t')
"""
it should return 
prefix does not exist
t not found
"""