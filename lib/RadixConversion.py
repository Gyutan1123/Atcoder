def base_10(num_n,n):
    """ n進数の数を10進数に変換

    Args:
        num_n (int): n新数の数
        n (int): 基数n
    Returns:
        int: num_nを10進数に変換した数
    """
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


def base_n(num_10,n):
    """ 10進数の数をn進数に変換

    Args:
        num_10 (int): 10進数の数
        n (int): 基数

    Returns:
        int: num_10をn進数に変換した数
    """
    if num_10 == 0:
        return 0
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])