import sys
import collections, heapq, string, math, itertools, copy, bisect
from sortedcontainers import SortedSet, SortedList, SortedDict

# pypyで再帰書く時のおまじない
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

II = lambda: int(input())
SI = lambda: input()
MI = lambda: map(int, input().split())
MS = lambda: input().split()
LI = lambda: list(MI())
LS = lambda: list(MS())

sys.setrecursionlimit(10**7)
mod = 10**9 + 7
########################################################

VOCAB_SIZE = 128
class TrieNode:
  def __init__(self,item=None):
    self.item = item
    self.children = [-1 for _ in range(VOCAB_SIZE)]
    self.subCnt = 0
  
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
    self.nodes[nodeIndex].subCnt += 1
    if nextNodeIndex == -1:
      newNode = TrieNode()
      nextNodeIndex = self.__add_node(newNode)
      self.nodes[nodeIndex].children[charNum] = nextNodeIndex
    
    if charIndex == len(word) - 1:
      self.nodes[nextNodeIndex].item = item
      self.nodes[nextNodeIndex].subCnt += 1
    
    else:
      self.insert(word, item, charIndex + 1, nextNodeIndex)
      
  
  def query(self, word):
    nodeIndex = 0
    node = self.nodes[nodeIndex]
    cnt = node.subCnt
    ret = 0
    depth = 0
    for c in word:
      node = self.nodes[nodeIndex]
      if cnt != node.subCnt:
        ret += (cnt-node.subCnt)*(depth-1)
      cnt = node.subCnt
      charNum = self.__get_char_num(c)
      nextNodeIndex = self.nodes[nodeIndex].children[charNum]
      if nextNodeIndex == -1:
        return None
      nodeIndex = nextNodeIndex
      depth += 1
      
    node = self.nodes[nodeIndex]
    if cnt != node.subCnt:
      ret += (cnt-node.subCnt)*(depth-1)
    
    ret += node.subCnt*(depth)
    
    return ret

trie = Trie()
n = II()
S = LS()

ans = 0

for s in S:
  trie.insert(s)
  
for s in S:
  ans += trie.query(s)
  
for s in S:
  ans -= len(s)

print(ans//2)  