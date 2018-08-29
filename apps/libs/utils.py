"""utils module"""
import string
import random


def get_random_string(length=28, digits=True):
    """
    返回随机字符串
    :param length: int, 随机字符串的长度
    :param digists: bool, 随机字符串是否包含数字
    :return: str
    """

    random_list = string.ascii_letters
    if digits:
        random_list = string.ascii_letters + string.digits
    lst = (random.choice(random_list) for i in range(length))
    return ''.join(lst)


def get_random_number(start=10000, stop=99999, is_str=True):
    """
    返回随机数，随机数的区间：[start, stop]
    :param start: int, 开始区间
    :param stop: int, 结束区间
    :param is_str: bool, 是否返回字符串
    :return: str or int, 如果 is_str 为 True 则返回字符串；否则，返回整数
    """

    num = random.randint(start, stop)
    return str(num) if is_str else num


def chunker(seq, step):
    """
    将列表分组，形成新的生成器，每个元素为 seq[start:start + step]
    :param seq: list/set, 等可以做 seq[start:end] 操作的数据类型
    :param step: int, seq 中每几个元素分成一组
    :return: 生成器
    """

    return (
        seq[start:start + step]
        for start in range(0, len(seq), step)
    )
