def Manacher(_s):
  """
    Manacherのアルゴリズムによって、
    回文の半径を求める。

    Args:
      _s : list (or String)
          元のリスト（文字列でも数値配列でも可）

    Returns:
      ans : list of int
          長さ (2*n - 1) の配列。
          i番目 (0-indexed) が表すのは、拡張後の_sにおける中心 i+1 の回文半径
          偶数位置が「要素間中心」、奇数位置が「要素上中心」に対応する。
  """
  
  n = len(_s)
  s = ['#']*(2*n+1)
  for i in range(n):
    s[2*i+1] = _s[i]
  
  n = 2*n+1
  
  ans = [0]*(n)
  i = 0
  w = 0
  while i < n:
    # iを中心に、同じ文字がどこまで連続するか
    while 0 <= i-w and i+w < n and s[i-w] == s[i+w]:
      w += 1
    ans[i] = w  
    
    # 回分の長さに応じて、利用可能な範囲を確認しつつメモする
    j = 1
    while 0 <= i-j and j+ans[i-j] < w:
      ans[i+j] = ans[i-j]
      j += 1

    # すでに計算が終わった分だけ中心と探索半径をずらす
    i += j
    w -= j
  
  # '#'分の補正
  for i in range(n):
    if i % 2 == 0:
      ans[i] = (ans[i]-1) // 2
    else:
      ans[i] //= 2
    
  return ans


print(Manacher('aabaa'))
print(Manacher('xaabbaa'))