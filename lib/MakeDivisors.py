def MakeDivisors(n):
  """ nの約数をO(√n)で列挙する
  https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56

  Args:
      n (int): 正整数

  Returns:
      list: nの約数を格納したリスト
  """
  lower_divisors , upper_divisors = [], []
  i = 1
  while i*i <= n:
    if n % i == 0:
      lower_divisors.append(i)
      if i != n // i:
        upper_divisors.append(n//i)
    i += 1
  return lower_divisors + upper_divisors[::-1]
