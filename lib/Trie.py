VOCAB_SIZE = 128
class TrieNode:
  def __init__(self,item=None):
    self.item = item
    self.children = [-1 for _ in range(VOCAB_SIZE)]
  
class Trie:
  def __init__(self):
    root = TrieNode()
    self.nodes = [root]
    
    
  def __add_node(self, node):
    self.nodes.append(node) 
    return len(self.nodes) - 1
  
  def __get_char_num(self,c):
    return ord(c) - ord('a')
    
  def insert(self, word, item='', charIndex=0, nodeIndex=0):
    charNum = self.__get_char_num(word[charIndex])
    nextNodeIndex = self.nodes[nodeIndex].children[charNum]
    if nextNodeIndex == -1:
      newNode = TrieNode()
      nextNodeIndex = self.__add_node(newNode)
      self.nodes[nodeIndex].children[charNum] = nextNodeIndex
    
    if charIndex == len(word) - 1:
      self.nodes[nextNodeIndex].item = item
    
    else:
      self.insert(word, item, charIndex + 1, nextNodeIndex)
      
  
  def query(self, word):
    nodeIndex = 0
    for c in word:
      charNum = self.__get_char_num(c)
      nextNodeIndex = self.nodes[nodeIndex].children[charNum]
      if nextNodeIndex == -1:
        return None
      nodeIndex = nextNodeIndex
    
    return self.nodes[nodeIndex].item

trie = Trie()
