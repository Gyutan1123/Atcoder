# 永続スタック
# https://qiita.com/wotsushi/items/72e7f8cdd674741ffd61
class PersistentStack:
  def __init__(self, value=None, prev=None):
    self.value = value
    self.prev = prev
  
  def top(self):
    return self.value
  
  def push(self,x):
    return PersistentStack(x, self)
  
  def pop(self):
    return self.prev